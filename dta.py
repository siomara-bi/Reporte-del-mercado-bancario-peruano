import pandas as pd
import os
import re

# --- CONFIGURACIÓN ---
mapa_bancos = {
    'BBVA': ['BBVA', 'CONTINENTAL'],
    'BCP': ['CREDITO', 'CRÉDITO', 'BCP'], # <--- AGREGADO CON TILDE
    'SCOTIABANK': ['SCOTIABANK'],
    'INTERBANK': ['INTERBANK'],
    'PICHINCHA': ['PICHINCHA', 'FINANCIERO'],
    'BANBIF': ['BIF', 'INTERAMERICANO'],
    'MIBANCO': ['MIBANCO'],
    'BANCOM': ['COMERCIO', 'BANCOM'],
    'GNB': ['GNB'],
    'FALABELLA': ['FALABELLA'],
    'SANTANDER': ['SANTANDER'],
    'RIPLEY': ['RIPLEY']
}

cuentas_interes = {
    'TOTAL_ACTIVOS': ['TOTAL ACTIVO', 'TOTAL DE ACTIVOS'],
    'CARTERA_CREDITOS': ['CARTERA DE CREDITOS NETA', 'COLOCACIONES NETAS'],
    'DEPOSITOS_TOTALES': ['DEPOSITOS', 'OBLIGACIONES CON EL PUBLICO'],
    'PATRIMONIO': ['PATRIMONIO', 'TOTAL PATRIMONIO'],
    'UTILIDAD_NETA': ['UTILIDAD NETA', 'RESULTADO NETO']
}

lista_datos = []
carpeta_input = 'input'

if not os.path.exists(carpeta_input):
    print(f" Error: No encuentro la carpeta '{carpeta_input}'.")
    exit()

archivos = [f for f in os.listdir(carpeta_input) if f.endswith('.xlsx') or f.endswith('.xls')]
print(f" Re-procesando {len(archivos)} archivos (Corrección BCP)...")

for archivo in archivos:
    try:
        match = re.search(r'(20\d{2})', archivo)
        if match:
            anio = int(match.group(1))
        else:
            continue

        if anio < 2018 or anio > 2024:
            continue

        mes = "12"
        if "se20" in archivo: mes = "09"
        elif "ju20" in archivo: mes = "06"
        elif "ma20" in archivo: mes = "03"
        
        fecha_reporte = f"30/{mes}/{anio}" if mes != "12" else f"31/{mes}/{anio}"
        ruta = os.path.join(carpeta_input, archivo)
        
        df = pd.read_excel(ruta, header=None, sheet_name=0)
        
        fila_header = -1
        for i in range(min(50, len(df))): 
            fila_texto = [str(x).upper() for x in df.iloc[i].values]
            if any('BBVA' in x for x in fila_texto) or any('CREDITO' in x for x in fila_texto) or any('CRÉDITO' in x for x in fila_texto):
                fila_header = i
                break
        
        if fila_header == -1:
            print(f"    No encontré cabecera en {archivo}")
            continue

        df.columns = [str(x).upper().strip() for x in df.iloc[fila_header].values]
        df = df.iloc[fila_header+1:].reset_index(drop=True)
        columna_cuentas = df.iloc[:, 0].astype(str).str.upper()

        for banco_estandar, alias_lista in mapa_bancos.items():
            col_banco_encontrada = None
            for col in df.columns:
                if any(alias in col for alias in alias_lista):
                    col_banco_encontrada = col
                    break
            
            if col_banco_encontrada:
                for cuenta_estandar, keywords_cuenta in cuentas_interes.items():
                    for keyword in keywords_cuenta:
                        filtro = columna_cuentas.str.contains(keyword, na=False)
                        if filtro.any():
                            valor = df.loc[filtro, col_banco_encontrada].iloc[0]
                            try: valor = float(valor)
                            except: valor = 0.0
                            lista_datos.append({
                                'fecha': fecha_reporte, 'anio': anio, 'mes': mes,
                                'banco': banco_estandar, 'indicador': cuenta_estandar, 'monto_miles': valor
                            })
                            break 
    except Exception as e:
        print(f"Error: {e}")

if lista_datos:
    df_final = pd.DataFrame(lista_datos)
    df_final = df_final.sort_values(by=['anio', 'banco'])
    df_final.to_csv('banca_consolidado_2018_2024.csv', index=False)
    print(f"\n ¡CORREGIDO! Archivo generado con {len(df_final)} registros (Incluyendo BCP).")