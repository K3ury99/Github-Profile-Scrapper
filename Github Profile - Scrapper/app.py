import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL del perfil de GitHub para los repositorios
username = "Shisui1601"
base_url = f"https://github.com/{username}?tab=repositories"
page = 1
repos_data = []

# Bucle para recorrer todas las páginas de repositorios
while True:
    url = f"{base_url}&page={page}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Encontrar los elementos que contienen los repositorios
    repo_elements = soup.find_all("h3", class_="wb-break-all")
    
    # Si no se encuentran más repositorios, detener el bucle
    if not repo_elements:
        break

    # Recopilar los nombres y enlaces de cada repositorio
    for repo_elem in repo_elements:
        name = repo_elem.a.text.strip()
        link = "https://github.com" + repo_elem.a["href"]
        repos_data.append((name, link))

    # Avanzar a la siguiente página de repositorios
    page += 1

# Crear un DataFrame de Pandas con los datos de los repositorios
repos_real_data = [
    {"Nombre": name, "Enlace": link}
    for name, link in repos_data
]

# Guardar los datos en un archivo Excel
excel_path = "repositorios_Shisui1601.xlsx"
df = pd.DataFrame(repos_real_data)
df.to_excel(excel_path, index=False)

print(f"Los datos fueron guardados exitosamente en: {excel_path}")


# Para probarlo solo hay que colcoar el nombre del GITHUB de la persona y colocarle el mismo nombre al 
# archivo que se genera de excel con el mismo nombre y listo, que disfruten!