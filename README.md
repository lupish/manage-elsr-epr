# Input files
The input file na
mes follow a structured format to encode specific parameters related to the dataset. The format is as follows:

> `datos_nT{nT}_nL{nL}_{u}{kv}{km}{kr}{hu}.dat`

Each component of the file name represents specific information:

- nT: number of periods.
- nL: number of customers.
- U:  Number of used items available in customers.
    - B = N(30, 6).
    - A = N(70, 14).
- Kv: Set-up cost of visiting customers.
    - B = 200.
    - M = 500.
    - A = 2000.
- Km: : Set-up cost of manufacturing in periods.
    - B = 200.
    - M = 500.
    - A = 2000.
- Kr: Set-up cost of remanufacturing in periods.
    - B = 200.
    - M = 500.
    - A = 1000.
- hu: Unit cost for holding inventory of used items in customers and periods.
    - B = 0.2.
    - M = 0.5.
    - A = 0.8.