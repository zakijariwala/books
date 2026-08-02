PY := venv/Scripts/python.exe
ASSETS := assets
BUILD := build
MANUSCRIPT := manuscript
STYLES := styles
GRAYSCALE_PROOF := $(ASSETS)/grayscale-proof
WORD_BUDGET := 28000

# Figure scripts import scripts/figstyle.py for shared print constraints.
# This must not be the repo root: a local diagrams/ directory would shadow
# the installed `diagrams` package.
export PYTHONPATH := scripts

METADATA := metadata.yaml
REFERENCE_DOCX := $(STYLES)/reference.docx
EPUB_CSS := $(STYLES)/epub.css

ARCH_SCRIPTS := $(wildcard diagrams/architecture/*.py)
FLOW_SOURCES := $(wildcard diagrams/flowcharts/*.mmd)
ARCH_PNGS := $(patsubst diagrams/architecture/%.py,$(ASSETS)/architecture/%.png,$(ARCH_SCRIPTS))
FLOW_PNGS := $(patsubst diagrams/flowcharts/%.mmd,$(ASSETS)/flowcharts/%.png,$(FLOW_SOURCES))

# Order matters and $(wildcard) sorts alphabetically, which would put
# back-matter.md before chapter one and front-matter.md after the last one.
# Build the list explicitly instead.
MD_BODY := $(sort $(wildcard $(MANUSCRIPT)/ch*.md))
MD_CHAPTERS := $(wildcard $(MANUSCRIPT)/front-matter.md) \
	$(MD_BODY) \
	$(wildcard $(MANUSCRIPT)/back-matter.md)

# Pandoc splits this on the platform's path separator: ';' on Windows, ':'
# elsewhere. Getting it wrong does not fail the build -- Pandoc warns
# "Could not fetch resource" for every figure and emits a book with no images.
ifeq ($(OS),Windows_NT)
PATH_SEP := ;
else
PATH_SEP := :
endif
RESOURCE_PATH := .$(PATH_SEP)$(ASSETS)$(PATH_SEP)$(ASSETS)/architecture$(PATH_SEP)$(ASSETS)/flowcharts

PANDOC_COMMON := $(METADATA) $(MD_CHAPTERS) \
	--resource-path=$(RESOURCE_PATH) \
	--toc \
	--top-level-division=chapter

.PHONY: all diagrams grayscale epub docx lint wordcount reference clean

all: diagrams lint epub docx

diagrams: $(ARCH_PNGS) $(FLOW_PNGS)

# figstyle.figure() normalizes to print spec on exit, so a figure rendered
# directly while iterating comes out identical to one built through make.
$(ASSETS)/architecture/%.png: diagrams/architecture/%.py scripts/figstyle.py
	@mkdir -p $(ASSETS)/architecture
	$(PY) $<

$(ASSETS)/flowcharts/%.png: diagrams/flowcharts/%.mmd scripts/mermaid-config.json
	@mkdir -p $(ASSETS)/flowcharts
	mmdc -i $< -o $@ -c scripts/mermaid-config.json -p scripts/mermaid-puppeteer-config.json -w 1350 -b white
	$(PY) scripts/normalize_image.py $@

grayscale: diagrams
	@mkdir -p $(GRAYSCALE_PROOF)
	@for f in $(ASSETS)/architecture/*.png $(ASSETS)/flowcharts/*.png; do \
		[ -f "$$f" ] || continue; \
		magick "$$f" -colorspace Gray "$(GRAYSCALE_PROOF)/$$(basename $$f)"; \
	done
	@echo "Grayscale proofs written to $(GRAYSCALE_PROOF)/"

# 6x9 interior template. Regenerate only when the trim size or margins change,
# which also means re-rendering every figure to match the new text block.
reference: $(REFERENCE_DOCX)

$(REFERENCE_DOCX): scripts/make_reference_docx.py
	$(PY) scripts/make_reference_docx.py

epub: diagrams
	@mkdir -p $(BUILD)
	pandoc $(PANDOC_COMMON) --css=$(EPUB_CSS) --epub-title-page=false -o $(BUILD)/book.epub

docx: diagrams $(REFERENCE_DOCX)
	@mkdir -p $(BUILD)
	pandoc $(PANDOC_COMMON) --reference-doc=$(REFERENCE_DOCX) -o $(BUILD)/book.docx
	$(PY) scripts/patch_docx.py $(BUILD)/book.docx

lint:
	vale --config=.vale.ini $(MANUSCRIPT)

wordcount:
	@$(PY) scripts/wordcount.py --budget $(WORD_BUDGET) $(MANUSCRIPT)

clean:
	rm -rf $(BUILD) $(ASSETS)
