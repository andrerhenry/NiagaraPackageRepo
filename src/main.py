from flask import Flask

app = Flask(__name__)

@app.route('/niagara/4.14/<package_name>', methods=['GET'])
def get_package(package_name:str):
    return print(f'Attempting to get: {package_name}')



def main():
    print("Hello from niagarapackagerepo!")


if __name__ == "__main__":
    main()
