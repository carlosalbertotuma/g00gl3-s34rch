import argparse
from googleapiclient.discovery import build

# Defina sua lista de pares de API_KEY e CSE_ID aqui
api_keys_and_ids = [
    {"API_KEY": 'SUAKEY', "CSE_ID": 'SEUCODIGOCSE1'},
    {"API_KEY": 'SUAKEY', "CSE_ID": 'SEUCODIGOCSE2'}
]

def search_google(query, start_index, num_results, api_key, cse_id):
    service = build("customsearch", "v1", developerKey=api_key)
    search_results = service.cse().list(q=query, cx=cse_id, start=start_index).execute()

    if 'items' in search_results:
        for i, result in enumerate(search_results['items'], start=start_index):
            print(f"{i}. {result['title']}")
            print(f"   {result['link']}")

def main():
    parser = argparse.ArgumentParser(description="Realize uma pesquisa no Google Custom Search em dois CSEs.")
    parser.add_argument("query", nargs='?', default=None, help="O termo de pesquisa (opcional)")
    args = parser.parse_args()

    if args.query is None:
        print(
            """
               __   __       _ ____       _____ _         _    
         __ _ /  \ /  \ __ _| |__ /___ __|__ / | | _ _ __| |_  
        / _` | () | () / _` | ||_ \___(_-<|_ \_  _| '_/ _| ' \ 
        \__, |\__/ \__/\__, |_|___/   /__/___/ |_||_| \__|_||_|
        |___/          |___/                                   
	
	By bl4dsc4n - v.01

        Por favor, forneça um termo de pesquisa como argumento.

        Exemplo: python3 g00gl3-s34rck.py "apache"
            """
        )
        return

    for pair in api_keys_and_ids:
        api_key = pair['API_KEY']
        cse_id = pair['CSE_ID']
        num_results_per_page = 10  # Apenas 10 resultados por página

        # Primeira pesquisa: itens 1-10
        search_google(args.query, 1, num_results_per_page, api_key, cse_id)

        # Segunda pesquisa: itens 11-20
        search_google(args.query, 11, num_results_per_page, api_key, cse_id)

        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
