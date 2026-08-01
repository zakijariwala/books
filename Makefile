PY := venv/Scripts/python.exe
ASSETS := assets
BUILD := build
MANUSCRIPT := manuscript
GRAYSCALE_PROOF := $(ASSETS)/grayscale-proof
WORD_BUDGET := 20000

ARCH_SCRIPTS := $(wildcard diagrams/architecture/*.py)
FLOW_SOURCES := $(wildcard diagrams/flowcharts/*.mmd)
ARCH_PNGS := $(patsubst diagrams/architecture/%.py,$(ASSETS)/architecture/%.png,$(ARCH_SCRIPTS))
FLOW_PNGS := $(patsubst diagrams/flowcharts/%.mmd,$(ASSETS)/flowcharts/%.png,$(FLOW_SOURCES))

MD_CHAPTERS := $(wildcard $(MANUSCRIPT)/*.md)

.PHONY: all diagrams grayscale epub docx lint wordcount clean

all: diagrams lint epub docx

diagrams: $(ARCH_PNGS) $(FLOW_PNGS)

$(ASSETS)/architecture/%.png: diagrams/architecture/%.py
	@mkdir -p $(ASSETS)/architecture
	$(PY) $<
	$(PY) scripts/normalize_image.py $@

$(ASSETS)/flowcharts/%.png: diagrams/flowcharts/%.mmd
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

epub: diagrams
	@mkdir -p $(BUILD)
	pandoc $(MD_CHAPTERS) -o $(BUILD)/book.epub --resource-path=.:$(ASSETS):$(ASSETS)/architecture:$(ASSETS)/flowcharts --metadata title="GCP Professional Cloud Architect Exam Prep"

docx: diagrams
	@mkdir -p $(BUILD)
	pandoc $(MD_CHAPTERS) -o $(BUILD)/book.docx --resource-path=.:$(ASSETS):$(ASSETS)/architecture:$(ASSETS)/flowcharts --metadata title="GCP Professional Cloud Architect Exam Prep"

lint:
	vale --config=.vale.ini $(MANUSCRIPT)

wordcount:
	@$(PY) scripts/wordcount.py --budget $(WORD_BUDGET) $(MANUSCRIPT)

clean:
	rm -rf $(BUILD) $(ASSETS)
