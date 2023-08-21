import aiomysql
import asyncio

async def show_vape():
    try:
        loop = asyncio.get_event_loop()
        conn = await aiomysql.connect(host='localhost', port=3306, 
                                    user='root', password='root',
                                    db='vape_db', loop=loop)
        cur = await conn.cursor()
        await cur.execute("SELECT * FROM vape")
        rows = await cur.fetchall()
        await cur.close()
        conn.close()

        result = "Одноразки:\n\n"

        for row in rows:
            result += f"ID: {row[0]}, Название: {row[1]}, Количество затяжек: {row[2]}, Вкус: {row[3]}," + \
            f"Цена: {row[4]}, Количество: {row[5]}\n\n"
        
        return result
    
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise SystemExit

async def show_vape_liquid():
    try:
        loop = asyncio.get_event_loop()
        conn = await aiomysql.connect(host='localhost', port=3306, 
                                    user='root', password='root',
                                    db='vape_db', loop=loop)
        cur = await conn.cursor()
        await cur.execute("SELECT * FROM vape_liquid")
        rows = await cur.fetchall()
        await cur.close()
        conn.close()

        result = "Жижи:\n\n"

        for row in rows:
            result += f"ID: {row[0]}, Название: {row[1]}, мг: {row[2]}, Вкус: {row[3]}," + \
            f"Цена: {row[4]}, Количество: {row[5]}\n\n"
        
        return result
        
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise SystemExit