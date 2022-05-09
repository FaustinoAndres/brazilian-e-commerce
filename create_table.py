from sqlite3 import Timestamp
from sqlalchemy import *
from config import host, port, database, user, password
conn_str = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()

city_state_table = Table('city_state_table', metadata,
    Column('city_state_id', INTEGER, primary_key=True),
    Column('city_state', VARCHAR(50)),
    Column('state_id', INTEGER)
)

code_zip_prefix_table = Table('code_zip_prefix_table', metadata,
    Column('code_zip_prefix_id', INTEGER, primary_key=True),
    Column('code_zip_prefix', INTEGER)
)

customers_table = Table('customers_table', metadata,
    Column('customer_id', VARCHAR(50), primary_key=True),
    Column('customer_unique_id', VARCHAR(50)),
    Column('customer_zip_code_prefix_id', INTEGER),
    Column('customer_city_id', INTEGER),
    Column('customer_state_id', INTEGER)
)

geolocation_table = Table('geolocation_table', metadata,
    Column('geolocation_id', INTEGER, primary_key=True),
    Column('geolocation_code_zip_prefix_id', INTEGER),
    Column('geolocation_lat', NUMERIC),
    Column('geolocation_lng', NUMERIC),
    Column('geolocation_city_state_id', INTEGER),
    Column('geolocation_state', INTEGER)
)

orders_table = Table('orders_table', metadata,
    Column('ID', String, primary_key=True),
    Column('order_id', Integer),
    Column('customer_id', VARCHAR(50)),
    Column('order_status', VARCHAR(50)),
    Column('order_purchase_timestamp', TIMESTAMP),
    Column('order_approved_at', TIMESTAMP),
    Column('order_delivered_carrier_date', TIMESTAMP),
    Column('order_delivered_customer_date', TIMESTAMP),
    Column('order_estimated_delivery_date', TIMESTAMP)
)

order_payments_table = Table('order_payments_table', metadata,
    Column('id', INTEGER, primary_key=True),
    Column('order_id', INTEGER),
    Column('payment_sequential', INTEGER),
    Column('payment_type', VARCHAR(50)),
    Column('payment_installments', INTEGER),
    Column('payment_value', NUMERIC)
)

order_reviews_table = Table('order_reviews_table', metadata,
    Column('id', INTEGER, primary_key=True),
    Column('review_id', VARCHAR(50)),
    Column('review_score', INTEGER),
    Column('review_comment_title', VARCHAR),
    Column('review_comment_message', VARCHAR),
    Column('review_creation_date', TIMESTAMP),
    Column('review_answer_timestamp', TIMESTAMP),
    Column('order_id', INTEGER)
)

product_category_name_table = Table('products_category_name_table', metadata,
    Column('category_id', INTEGER, primary_key=True),
    Column('product_category_name', VARCHAR(50)),
    Column('product_category_name_english', VARCHAR(50))
)

products_table = Table('products_table', metadata,
    Column('product_id', VARCHAR, primary_key=True),
    Column('product_category_name_id', INTEGER),
    Column('product_name_lenght', INTEGER),
    Column('product_description_lenght', INTEGER),
    Column('product_photos_qty', INTEGER),
    Column('product_weight_g', INTEGER),
    Column('product_length_cm', INTEGER),
    Column('product_height_cm', INTEGER),
    Column('product_width_cm', INTEGER)
)

sellers_table = Table('sellers_table', metadata,
    Column('seller_id', VARCHAR, primary_key=True),
    Column('seller_code_zip_prefix_id', INTEGER),
    Column('seller_city_state_id', INTEGER),
    Column('seller_state_id', INTEGER)
)

state_table = Table('state_table', metadata,
    Column('state_id', INTEGER, primary_key=True),
    Column('state', VARCHAR(2))
)

unique_order_id_table = Table('unique_order_id_table', metadata,
    Column('order_id', INTEGER, primary_key=True),
    Column('order', VARCHAR(50))
)

order_items_table = Table('order_items_table', metadata,
    Column('id', INTEGER, primary_key=True),
    Column('order_id', INTEGER),
    Column('item_id', INTEGER),
    Column('product_id', VARCHAR),
    Column('seller_id', VARCHAR),
    Column('shipping_limit_date', TIMESTAMP),
    Column('price', NUMERIC),
    Column('freight_value', NUMERIC)
)

metadata.create_all(engine)
#ResultProxy = connection.execute(query)