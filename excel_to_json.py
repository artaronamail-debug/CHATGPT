#!/usr/bin/env python3
"""
SCRIPT UNIVERSAL - Convierte CUALQUIER Excel de propiedades a JSON
"""

import pandas as pd
import json
import os

def excel_a_json_universal():
    print("🔄 CONVIRTIENDO Excel a JSON (Modo Universal)")
    print("=" * 50)
    
    # Archivos
    excel_file = "propiedades.xlsx"
    json_file = "properties.json"
    
    # 1. Verificar que existe el Excel
    if not os.path.exists(excel_file):
        print(f"❌ ERROR: No encuentro '{excel_file}'")
        print("💡 Asegúrate de que el archivo esté en la misma carpeta")
        input("Presiona Enter para salir...")
        return False
    
    try:
        # 2. Leer el Excel (hoja principal)
        print(f"📖 Leyendo {excel_file}...")
        
        # Intentar leer la primera hoja
        df = pd.read_excel(excel_file)
        
        print(f"✅ Excel leído correctamente")
        print(f"📊 Filas: {len(df)}")
        print(f"📋 Columnas encontradas: {list(df.columns)}")
        print()
        
        # 3. Mostrar mapeo de columnas
        print("🔍 MAPEO AUTOMÁTICO DE COLUMNAS:")
        print("-" * 30)
        
        mapeo_columnas = {
            'titulo': ['titulo', 'title', 'nombre', 'propiedad'],
            'barrio': ['barrio', 'neighborhood', 'zona', 'ubicacion'],
            'precio': ['precio', 'price', 'valor', 'costo'],
            'ambientes': ['ambientes', 'rooms', 'habitaciones', 'dormitorios'],
            'metros': ['metros', 'sqm', 'metros_cuadrados', 'superficie'],
            'operacion': ['operacion', 'tipo_operacion', 'venta_alquiler'],
            'tipo': ['tipo', 'tipo_propiedad', 'categoria'],
            'descripcion': ['descripcion', 'description', 'detalles']
        }
        
        columnas_mapeadas = {}
        
        for columna in df.columns:
            col_lower = str(columna).lower()
            for clave, posibles in mapeo_columnas.items():
                if any(p in col_lower for p in posibles):
                    columnas_mapeadas[clave] = columna
                    print(f"   ✅ '{columna}' → {clave}")
                    break
            else:
                print(f"   📝 '{columna}' → (campo adicional)")
                columnas_mapeadas[columna] = columna
        
        print()
        
        # 4. Convertir a JSON
        propiedades = []
        
        for index, row in df.iterrows():
            propiedad = {
                "id": index + 1,
                "title": obtener_valor(row, columnas_mapeadas, 'titulo', f"Propiedad {index + 1}"),
                "neighborhood": obtener_valor(row, columnas_mapeadas, 'barrio', '').lower(),
                "price": float(obtener_valor(row, columnas_mapeadas, 'precio', 0)),
                "rooms": int(obtener_valor(row, columnas_mapeadas, 'ambientes', 1)),
                "sqm": float(obtener_valor(row, columnas_mapeadas, 'metros', 0)),
                "description": obtener_valor(row, columnas_mapeadas, 'descripcion', ''),
                "operacion": obtener_valor(row, columnas_mapeadas, 'operacion', 'alquiler').lower(),
                "tipo": obtener_valor(row, columnas_mapeadas, 'tipo', 'departamento').lower(),
            }
            
            # Agregar TODAS las columnas adicionales
            for columna in df.columns:
                if columna not in columnas_mapeadas.values() or columna not in mapeo_columnas.keys():
                    valor = row[columna]
                    if not pd.isna(valor):
                        propiedad[str(columna).lower()] = str(valor)
            
            propiedades.append(propiedad)
            print(f"   ✅ Procesada: {propiedad['title']}")
        
        # 5. GUARDAR JSON (sobrescribe el anterior)
        print(f"\n💾 Guardando {len(propiedades)} propiedades en {json_file}...")
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(propiedades, f, ensure_ascii=False, indent=2)
        
        # 6. Mostrar resumen
        print(f"\n🎉 ¡CONVERSIÓN EXITOSA!")
        print("=" * 30)
        print(f"📈 Total propiedades: {len(propiedades)}")
        
        # Estadísticas simples
        operaciones = {}
        barrios = {}
        for prop in propiedades:
            op = prop["operacion"]
            barrio = prop["neighborhood"]
            operaciones[op] = operaciones.get(op, 0) + 1
            if barrio:
                barrios[barrio] = barrios.get(barrio, 0) + 1
        
        print(f"🏢 Operaciones: {operaciones}")
        print(f"📍 Barrios: {len(barrios)} diferentes")
        
        # Mostrar primeras 3 propiedades como ejemplo
        print(f"\n🔍 MUESTRA (primeras 3 propiedades):")
        for i, prop in enumerate(propiedades[:3]):
            print(f"   {i+1}. {prop['title']}")
            print(f"      📍 {prop['neighborhood']} | 🏢 {prop['operacion']} | 💰 ${prop['price']:,.0f}")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        print("💡 ¿El archivo Excel está abierto? Ciérralo e intenta de nuevo.")
        return False

def obtener_valor(row, mapeo, clave, default):
    """Obtiene valor de una fila usando el mapeo de columnas"""
    if clave in mapeo:
        columna = mapeo[clave]
        valor = row[columna]
        if pd.isna(valor):
            return default
        return str(valor) if isinstance(default, str) else valor
    return default

def crear_excel_ejemplo():
    """Crea un Excel de ejemplo si no existe"""
    ejemplo_file = "propiedades_ejemplo.xlsx"
    
    if not os.path.exists(ejemplo_file):
        print(f"\n📝 Creando Excel de ejemplo: {ejemplo_file}")
        
        datos = [
            {
                "titulo": "Departamento en Palermo",
                "barrio": "Palermo",
                "precio": 250000,
                "ambientes": 2,
                "metros": 65,
                "operacion": "alquiler",
                "tipo": "departamento",
                "descripcion": "Hermoso departamento con balcón",
                "direccion": "Honduras 1234",
                "expensas": 8000,
                "cochera": "Sí",
                "acepta_mascotas": "Sí"
            },
            {
                "titulo": "Casa en Belgrano", 
                "barrio": "Belgrano",
                "precio": 450000,
                "ambientes": 3,
                "metros": 110,
                "operacion": "venta",
                "tipo": "casa",
                "descripcion": "Casa familiar con jardín",
                "direccion": "Juramento 5678",
                "expensas": 0,
                "cochera": "Sí",
                "acepta_mascotas": "No"
            },
            {
                "titulo": "PH en Colegiales",
                "barrio": "Colegiales", 
                "precio": 180000,
                "ambientes": 1,
                "metros": 45,
                "operacion": "alquiler",
                "tipo": "ph",
                "descripcion": "PH acogedor ideal para una persona",
                "direccion": "Conesa 910",
                "expensas": 2000,
                "cochera": "No",
                "acepta_mascotas": "Sí"
            }
        ]
        
        df = pd.DataFrame(datos)
        df.to_excel(ejemplo_file, index=False)
        print(f"✅ Excel de ejemplo creado: {ejemplo_file}")
        print("💡 Puedes usar este archivo como referencia")

if __name__ == "__main__":
    print("🔄 CONVERSOR UNIVERSAL - Excel a JSON")
    print("=" * 50)
    print("Este script convierte CUALQUIER Excel de propiedades a JSON")
    print()
    
    # Crear ejemplo si no hay archivo
    if not os.path.exists("propiedades.xlsx"):
        crear_excel_ejemplo()
        print(f"\n📁 Ahora edita 'propiedades_ejemplo.xlsx' con tus datos")
        print("   y renómbralo a 'propiedades.xlsx'")
        input("\nPresiona Enter para salir...")
    else:
        # Ejecutar conversión
        success = excel_a_json_universal()
        
        if success:
            print(f"\n✅ ¡LISTO! Ahora reinicia el servidor para cargar las nuevas propiedades.")
        else:
            print(f"\n❌ No se pudo completar la conversión.")
        
        input("\nPresiona Enter para salir...")