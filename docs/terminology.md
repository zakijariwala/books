# Terminology

One approved definition per term, in plain language, vendor-neutral. When a
chapter first uses a term, it defines it the way it is defined here, then never
re-defines it. New terms get added here before they enter a draft.

> **Author review required.** These are seeded definitions. TASKS.md marks this
> file as one that does not survive being left to a model. Read every line, cut
> the terms the book will not use, and rewrite any definition that is not how you
> would say it out loud. The definitions set the book's precision; they should
> sound like the narrator, not a glossary.

Rules for a good definition here:
- Plain enough that the second-layer reader (buyer.md) gets it with no job.
- No dollars, no rate cards. Cost is described as shape.
- One approved analogy per term, drawn from the approved set (airports,
  warehouses, hotels, utilities, transportation, supply chains).

---

| Term | Definition | Analogy | First used |
|------|-----------|---------|-----------|
| The cloud | Renting computers you never see, by the hour, in someone else's building, instead of buying and housing your own. | A utility: you pay for the electricity you use, not for the power station. | 1 |
| Server | A computer that runs all the time and answers requests from other computers, rather than one a person sits in front of. | A cook in a kitchen taking orders, not a diner eating. | 1 |
| Capital expense (capex) | Money spent up front to own a thing for years. Buying the building. | Buying a delivery van. | 1 |
| Operating expense (opex) | Money spent as you go, for as long as you use the thing. Renting by the hour. | Hailing a taxi. | 1 |
| Region | A cluster of data centers in one part of the world where your data and computers physically sit. | A city where a company keeps a warehouse. | 3 |
| Availability zone | A separate building inside a region, wired so that one failing does not take the others down. | Separate loading docks at the same port. | 3 |
| Data residency | The question of which country your data physically lives in, and whose laws reach it. | Which country a warehouse sits in, and whose customs apply. | 3 |
| Shared responsibility | The split between what the landlord secures (the building) and what you secure (what you put in it). | A storage unit: they lock the gate, you lock your unit. | 3 |
| Compute | The rented machine that does the actual work of running your software. | Renting brains by the hour. | 4 |
| Instance | One rented machine of a chosen size. Bigger instance, more work per second, larger bill. | Booking a bigger truck for a bigger load. | 4 |
| GPU | A specialized, scarce, power-hungry chip that does the math behind modern AI far faster than an ordinary one. | A specialist crane at a port: rare, expensive, and everyone wants it at once. | 4 |
| Storage | Keeping files somewhere they can be retrieved later. Cheap to keep, not always cheap to move. | A warehouse: shelving a pallet is cheap, shipping it out is not. | 5 |
| Egress | The cost of moving data out of the cloud or between regions. | The freight bill, not the storage bill. | 5 |
| Latency | The delay between asking for something and getting it, driven partly by physical distance. | The wait for a package from a far-off warehouse. | 6 |
| Read replica | A copy of a database kept for reading, so the main copy is not overwhelmed by everyone looking at once. | A second reference desk that only answers questions, never files new records. | 7 |
| Replication lag | The short delay before a change on the main copy shows up on the read copy. | The gap before every branch of a chain has the updated catalogue. | 7 |
| Autoscaling | Capacity that grows when demand rises and shrinks when it falls, so you pay for what you use. | Opening more checkout lanes at the rush, closing them after. | 8 |
| Serverless | Paying per request for work, with no machine to keep running between requests. | A vending machine: it costs nothing between sales. | 8 |
| SLA (service level agreement) | The vendor's written promise about uptime, and, more importantly, what it does not cover. | A courier's delivery guarantee, with the fine print. | 9 |
| Blast radius | How far the damage spreads if one part is compromised. Security measured as containment, not as a wall. | Watertight compartments in a ship's hull. | 10 |
| Cost shape | Which line on the bill dominates, which surprises, and which grows with users versus with data. | Reading a utility bill by what drives each charge, not the total. | 11 |
| Lock-in | What it would cost in time and rewritten work to leave one vendor for another. | The cost of moving warehouses when your shelving only fits one building. | 11 |
