movies=[{"id": 1, "title": "Matrix", "available": "true"}, 
        {"id": 2, "title": "Inception", "available": "true"},
        {"id": 3, "title": "Tenet", "available": "true"}]

customers={1: {"name": "Ajay", "rented": []}, 
           2: {"name": "Abhay", "rented": []}}

transactions = []

def rent_movie(customer_id, movie_id):
    movie = next((m for m in movies if m["id"]==movie_id and m["available"]), None)
    if movie:
        movie["available"]=False
        customers[customer_id]["rented"].append(movie["title"])
        transactions.append({"cust": customer_id, "movie": movie_id, "action": "rented"})
        print(f"{customers[customer_id]['name']} rented '{movie['title']}'.")
    if not movie["available"]:
        print(f"Movie'{movie['title']}' is already rented out.")
        return
    
def return_movie(cust_id, movie_id):
    movie = next((m for m in movies if m["id"]==movie_id), None)
    if movie and not movie["available"]:
        movie["available"]=True
        customers[cust_id]["rented"].remove(movie["title"])
        transactions.append({"cust": cust_id, "movie": movie_id, "action": "returned"})
        print(f"{customers[cust_id]['name']} returned '{movie['title']}'.")

def rental_report():
    for t in transactions:
        action ="rented" if t["action"]=="rented" else "returned"
    print(f"{customers[t['cust']]['name']} {action} '{next(m['title'] for m in movies if m['id']==t['movie'])}'.")


rent_movie(1,2)
return_movie(1,2)
rental_report(1,2)
