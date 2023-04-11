# agent-based-example

This repository provides an example of generating a dataset with an agent-based approach. The dataset contains customer purchase histories, and is created by simulating interactions between products, customers, and stores.

## Contents

- main.py: The main script responsible for generating the TRANSACTIONS table using an agent-based approach.
- params.yaml: A configuration file containing various parameters that can be used to fine-tune the generation of the TRANSACTIONS table.
- PRODUCTS.csv: A synthetically generated table containing information about various products.
- CUSTOMERS.csv: A synthetically generated table containing information about customers.
- STORES.csv: A synthetically generated table containing information about stores.
- TRANSACTIONS.csv: The output file containing the generated customer purchase histories.

## Usage
To generate the TRANSACTIONS table, simply run the main.py script:

```bash
python main.py
```

This will produce a TRANSACTIONS.csv file containing customer purchase histories generated using the agent-based approach.

Configuration
You can customize the dataset generation by modifying the parameters in the params.yaml file. Some of the parameters you can adjust include:

- num_transactions: The total number of transactions to generate.
- min_products_per_transaction: The minimum number of products per transaction.
- max_products_per_transaction: The maximum number of products per transaction.
- n_days: number of days covered by the simulation.
- n_customers: number of agents to include in the simulation.
- price_propensity[1-10]: this coefficient can be used to tune the probability distribution defining the probability of a purchase as a function of the product price (see docs for more details). 
- income_propensity[0-0.8]: this coefficient defines a modifier to the purchase propensity based on the agent income (see docs for more details).