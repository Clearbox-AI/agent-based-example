import pandas as pd
from utils import generate_datetime_string, generate_days, distances
import numpy as np
import yaml
from tqdm import tqdm


def main():

    with open('params.yaml', 'r') as file:
            params_data = yaml.safe_load(file)

    n_customers = params_data['n_customers']
    price_propensity = params_data['price_propensity']
    income_propensity = params_data['income_propensity']
    days = generate_days(params_data['n_days'])
    df = pd.read_csv('CUSTOMERS.csv')
    df1 = pd.read_csv('PRODUCTS.csv')

    shops = ['Brussels', 'Ghent', 'Liege']
    bikes = df1[df1['category']=='Bikes']['product']
    transactions = []
    listprods = list(df1['category'].unique())
    listprods.remove('Bikes')
    listprods_b = list(df1['category'].unique())
    listprods_b.remove('Bikes')
    listprods_b.remove('Wheels')
    listprods_b.remove('Pedals')
    listprods_b.remove('Handlebars & Grips')
    listprods_b.remove('Brakes')
    listprods_b.remove('Gears & Drivetrains')
    listprods_b
    w = 0
    tot_bikes=0
    print('Generating data...')
    for i in tqdm(range(min(n_customers, df.shape[0]))):
        high_income = df.iloc[i]['high_income']
        day = generate_datetime_string(np.random.choice(days))
        #print(i,day)
        d=np.array(list(distances[df.iloc[i]['city']].values()))
        pshop = 1./(d+1.)
        pshop = pshop/pshop.sum()    
        shop = np.random.choice([1, 2, 3], p=pshop)

        if (df.iloc[i]['has_bicycle']==0)&(np.random.randn()>0.85):
            prices = df1[df1['category']=='Bikes']['MSRPprice']
            p_bike = (1/prices)
            p_bike = p_bike/p_bike.sum()
            bike_model = np.random.choice(bikes,p=p_bike)
            bike_id = df1[df1['product']==bike_model]['product_id'].values[0]
            discount = df1[df1['product']==bike_model]['discount'].values[0]/100 + df.iloc[i]['has_insurance'].astype(int)*0.05
            qty = 1
            price = df1[df1['product']==bike_model]['MSRPprice'].values[0]
            paid = price * (1.-discount)
            transaction_dict = {'transaction_id': int(pd.to_datetime(day).timestamp()),
                                                    'date':day,
                                                    'shop_id':shop,
                                                    'customer_id': i, 
                                                    'product_id': bike_id,
                                                    'quantity': qty,
                                                    'applied_discount': discount,
                                                    'total_amount': price,
                                                    'paid':paid,
                                                    'payment_type': 'CARD'}
            w+=1
            tot_bikes+=1
            transactions.append(transaction_dict)
            pay_type = 'CARD'
            for j in listprods_b:
                if np.random.rand()>0.9-income_propensity*high_income:
                    prod = df1[df1['category']==j]['product']
                    prices = df1[df1['category']==j]['MSRPprice']
                    p_prod = (1/prices**price_propensity)
                    p_prod = p_prod/p_prod.sum()    
                    prod_model = np.random.choice(prod,p=p_prod)
                    prod_id = df1[df1['product']==prod_model]['product_id'].values[0]
                    discount = df1[df1['product']==prod_model]['discount'].values[0]/100 + df.iloc[i]['has_insurance'].astype(int)*0.05
                    price = df1[df1['product']==prod_model]['MSRPprice'].values[0]
                    if price < 100:
                        qty = np.random.choice([1,2,3],p=[0.5,0.3,0.2]) 
                    else:
                        qty = 1

                    paid = qty * price * (1.-discount)

                    transaction_dict = {'transaction_id': int(pd.to_datetime(day).timestamp()),
                                                            'date':day,
                                                            'shop_id':shop,
                                                            'customer_id': i, 
                                                            'product_id': prod_id,
                                                            'quantity': qty,
                                                            'applied_discount': discount,
                                                            'total_amount': qty * price,
                                                            'paid':paid,
                                                            'payment_type': pay_type}
                    w+=1                                                    
                    transactions.append(transaction_dict)
        else:
            if (high_income==0)&(df.iloc[i]['has_bicycle']==1)&(np.random.randn()>0.9):
                pay_type = 'CASH'
            else:
                pay_type = 'CARD'
            for j in listprods:
                if np.random.rand()>0.9-income_propensity*high_income:
                    prod = df1[df1['category']==j]['product']
                    prices = df1[df1['category']==j]['MSRPprice']
                    p_prod = (1/prices**price_propensity)
                    p_prod = p_prod/p_prod.sum()

                    prod_model = np.random.choice(prod,p=p_prod)
                    prod_id = df1[df1['product']==prod_model]['product_id'].values[0]

                    discount = df1[df1['product']==prod_model]['discount'].values[0]/100 + df.iloc[i]['has_insurance'].astype(int)*0.05
                    price = df1[df1['product']==prod_model]['MSRPprice'].values[0]
                    if price < 100:
                        qty = np.random.choice([1,2,3],p=[0.5,0.3,0.2]) 
                    else:
                        qty = 1

                    paid = qty * price * (1.-discount)

                    transaction_dict = {'transaction_id': int(pd.to_datetime(day).timestamp()),
                                                            'date':day,
                                                            'shop_id':shop,
                                                            'customer_id': i, 
                                                            'product_id': prod_id,
                                                            'quantity': qty,
                                                            'applied_discount': discount,
                                                            'total_amount': qty * price,
                                                            'paid':paid,
                                                            'payment_type': pay_type}
                    w+=1                                                    
                    transactions.append(transaction_dict)

    dft = pd.DataFrame(transactions)
    dft['dt']=pd.to_datetime(dft['date'], format='%d/%m/%Y %H:%M')
    dft = dft.sort_values(by=['dt'])

    for i in dft['customer_id'].unique():
        if np.random.rand()>0.8:
            dft.loc[dft['customer_id'] == i, 'customer_id'] = 'N/A'
            
    dft['transaction_id']=dft['transaction_id']-1147090300
    dft = dft.drop(['dt'],axis=1)
    dft.to_csv('TRANSACTIONS.csv',index=False)

if __name__ == "__main__":
    main()
    print('Generated TRANSACTIONS.csv file.')