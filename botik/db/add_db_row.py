import aiomysql
import asyncio

async def add_row_vape(brand, number_of_pulls, flavor, price, quantity):
    try:
        loop = asyncio.get_event_loop()
        conn = await aiomysql.connect(host='localhost', port=3306, 
                                    user='root', password='root',
                                    db='vape_db', loop=loop)
        cur = await conn.cursor()
        await cur.execute("INSERT INTO vape (brand, number_of_pulls, flavor, price, quantity)" + \
                          "VALUES (%s, %d, %s, %f, %d)", (brand, number_of_pulls, flavor, price, quantity))
        await cur.close()
        conn.close()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise SystemExit
    
async def add_row_vape_liquid(brand, liquid_mg, flavor, price, quantity):
    try:
        loop = asyncio.get_event_loop()
        conn = await aiomysql.connect(host='localhost', port=3306, 
                                    user='root', password='root',
                                    db='vape_db', loop=loop)
        cur = await conn.cursor()
        await cur.execute("INSERT INTO vape (brand, liquid_mg, flavor, price, quantity)" + \
                          "VALUES (%s, %d, %s, %f, %d)", (brand, liquid_mg, flavor, price, quantity))
        await cur.close()
        conn.close()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise SystemExit