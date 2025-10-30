# Sistema Basado en Reglas para Diagnóstico de Vehículos

**Autor:** Rubén Jiménez  
**Fecha:** Octubre 2025

---

## Tabla de Contenidos

- [Introducción](#introducción)
- [Enunciado del Ejercicio](#enunciado-del-ejercicio)
- [Diseño del Sistema](#diseño-del-sistema)
- [Implementación](#implementación)
- [Ejemplos de Ejecución](#ejemplos-de-ejecución)
- [Análisis del Sistema](#análisis-del-sistema)
- [Conclusiones](#conclusiones)
- [Referencias](#referencias)

---

## Introducción

Los sistemas basados en reglas son un tipo de sistema experto que utiliza un conjunto de reglas condicionales (IF-THEN) para tomar decisiones o realizar diagnósticos. En este proyecto se presenta un sistema de diagnóstico de problemas en vehículos implementado en Python.

### Objetivos

- Diseñar un sistema basado en reglas para diagnóstico automotriz
- Implementar el sistema en Python utilizando estructuras condicionales
- Proporcionar diagnósticos precisos basados en síntomas reportados

---

## Enunciado del Ejercicio

**ACTIVIDAD 4.- Diseña tu propio Sistema basado en reglas y prográmalo en Python.**

1. Escoge o diseña un sistema basado en reglas
2. Prográmalo en Python de tal forma que la respuesta sea la esperada

### Sistema Seleccionado

Se ha diseñado un sistema de diagnóstico de problemas en vehículos que, mediante una serie de preguntas al usuario, identifica posibles fallas y proporciona recomendaciones de reparación.

---

## Diseño del Sistema

### Reglas del Sistema

El sistema implementa las siguientes reglas principales:

#### 1️ **SI** el vehículo enciende **Y** hace ruidos **ENTONCES** diagnosticar según ubicación del ruido

- **Motor**: Problema en el motor (correa, aceite, distribución)
- **Frenos**: Problema en frenos (pastillas, discos) -  URGENTE
- **Suspensión**: Problema en suspensión (amortiguadores)

#### 2️ **SI** el vehículo enciende **Y** no hace ruidos **ENTONCES** evaluar rendimiento

- **Alto consumo**: Filtros, inyectores, neumáticos
- **Pérdida de potencia**: Bujías, sensores, filtros
- **Humo**: Aceite, pistones, compresión

#### 3️ **SI** el vehículo no enciende **Y** hace sonido **ENTONCES** problema eléctrico o combustible

- **Sonido "clic"**: Batería descargada
- **Motor intenta arrancar**: Problema de combustible o chispa

#### 4️ **SI** el vehículo no enciende **Y** no hace sonido **ENTONCES** batería o sistema eléctrico

- **Luces del tablero SÍ encienden**: Motor de arranque dañado
- **Luces del tablero NO encienden**: Batería completamente descargada

###  Diagrama de Flujo

```
¿El vehículo ENCIENDE?
│
├─ SÍ → ¿Hace RUIDOS extraños?
│       ├─ SÍ → ¿Dónde? (motor/frenos/suspensión)
│       │       ├─ Motor → Problema en motor
│       │       ├─ Frenos → Problema en frenos (URGENTE)
│       │       └─ Suspensión → Problema en suspensión
│       │
│       └─ NO → ¿Problemas de RENDIMIENTO?
│               ├─ SÍ → ¿Qué problema? (consumo/potencia/humo)
│               └─ NO → Vehículo en buen estado
│
└─ NO → ¿Hace SONIDO al girar llave?
        ├─ SÍ → ¿Qué tipo? (clic/arranque)
        │       ├─ Clic → Batería descargada
        │       └─ Arranque → Problema combustible/chispa
        │
        └─ NO → ¿Luces del tablero encienden?
                ├─ SÍ → Motor de arranque dañado
                └─ NO → Batería muerta/desconectada
```

---

##  Implementación

### Uso

```bash
python diagnostico_vehiculos.py
```

### Código Completo

```python
# Sistema basado en reglas para diagnóstico de problemas en vehículos

print("=== SISTEMA DE DIAGNÓSTICO DE VEHÍCULOS ===\n")
print("Bienvenido al sistema de diagnóstico automotriz")
print("Responda las preguntas para identificar el problema\n")

# Primera pregunta: ¿El vehículo enciende?
print("¿El vehículo enciende? (si/no)")
enciende = input().lower()

if enciende == "si":
    # Segunda pregunta: ¿Hace ruidos extraños?
    print("¿El vehículo hace ruidos extraños? (si/no)")
    ruidos = input().lower()
    
    if ruidos == "si":
        # Tercera pregunta: ¿Dónde se escucha el ruido?
        print("¿Dónde se escucha el ruido? (motor/frenos/suspension)")
        ubicacion = input().lower()
        
        if ubicacion == "motor":
            print("\n DIAGNÓSTICO: Problema en el MOTOR")
            print("   - Posibles causas: correa desgastada, falta de aceite, cadena de distribución")
            print("   - Recomendación: Revisar nivel de aceite y llevar a mecánico")
        elif ubicacion == "frenos":
            print("\n DIAGNÓSTICO: Problema en los FRENOS")
            print("   - Posibles causas: pastillas gastadas, discos desgastados")
            print("   - Recomendación: ¡URGENTE! Revisar sistema de frenos inmediatamente")
        elif ubicacion == "suspension":
            print("\n DIAGNÓSTICO: Problema en la SUSPENSIÓN")
            print("   - Posibles causas: amortiguadores dañados, barra estabilizadora")
            print("   - Recomendación: Revisar amortiguadores y tren delantero")
        else:
            print("\n DIAGNÓSTICO: Revisar otras áreas del vehículo")
    
    else:
        # No hace ruidos
        print("¿Tiene problemas de rendimiento? (si/no)")
        rendimiento = input().lower()
        
        if rendimiento == "si":
            print("¿Qué problema presenta? (consumo/potencia/humo)")
            problema = input().lower()
            
            if problema == "consumo":
                print("\n DIAGNÓSTICO: ALTO CONSUMO de combustible")
                print("   - Posibles causas: filtro de aire sucio, inyectores, presión de neumáticos")
                print("   - Recomendación: Revisar filtros y sistema de inyección")
            elif problema == "potencia":
                print("\n DIAGNÓSTICO: PÉRDIDA DE POTENCIA")
                print("   - Posibles causas: filtros sucios, bujías, sensor MAF")
                print("   - Recomendación: Hacer mantenimiento general y diagnóstico electrónico")
            elif problema == "humo":
                print("\n DIAGNÓSTICO: Emisión de HUMO anormal")
                print("   - Posibles causas: aceite quemándose, problemas en pistones")
                print("   - Recomendación: Revisar nivel de aceite y compresión del motor")
            else:
                print("\n DIAGNÓSTICO: Requiere revisión detallada")
        else:
            print("\n✓ DIAGNÓSTICO: El vehículo está en BUEN ESTADO")
            print("   - Recomendación: Continuar con mantenimiento preventivo regular")

else:
    # El vehículo NO enciende
    print("¿Hace algún sonido al girar la llave? (si/no)")
    sonido = input().lower()
    
    if sonido == "si":
        print("¿Qué tipo de sonido hace? (clic/arranque/nada)")
        tipo_sonido = input().lower()
        
        if tipo_sonido == "clic":
            print("\n DIAGNÓSTICO: Problema de BATERÍA")
            print("   - Posibles causas: batería descargada o dañada")
            print("   - Recomendación: Cargar o reemplazar la batería")
        elif tipo_sonido == "arranque":
            print("\n DIAGNÓSTICO: Problema de COMBUSTIBLE o CHISPA")
            print("   - Posibles causas: falta de gasolina, bomba de combustible, bujías")
            print("   - Recomendación: Verificar nivel de combustible y sistema de encendido")
        else:
            print("\n DIAGNÓSTICO: Problema ELÉCTRICO severo")
            print("   - Recomendación: Revisar fusibles y sistema eléctrico completo")
    else:
        print("¿Las luces del tablero encienden? (si/no)")
        luces = input().lower()
        
        if luces == "si":
            print("\n DIAGNÓSTICO: Problema en el MOTOR DE ARRANQUE")
            print("   - Posibles causas: motor de arranque dañado, relay defectuoso")
            print("   - Recomendación: Revisar motor de arranque y conexiones")
        else:
            print("\n DIAGNÓSTICO: BATERÍA COMPLETAMENTE DESCARGADA o desconectada")
            print("   - Posibles causas: batería muerta, terminales flojos/corroídos")
            print("   - Recomendación: Revisar conexiones de batería y estado de carga")

print("\n" + "="*50)
print("¡Gracias por usar el sistema de diagnóstico!")
print("Recuerde: Este es un diagnóstico preliminar.")
print("Siempre consulte con un mecánico profesional.")
print("="*50)
```

---

## Ejemplos de Ejecución

### Caso 1: Batería Descargada

**Entrada del usuario:**
```
¿El vehículo enciende? no
¿Hace algún sonido al girar la llave? si
¿Qué tipo de sonido hace? clic
```

**Salida del sistema:**
```
 DIAGNÓSTICO: Problema de BATERÍA
   - Posibles causas: batería descargada o dañada
   - Recomendación: Cargar o reemplazar la batería
```

---

### Caso 2: Problema en Frenos

**Entrada del usuario:**
```
¿El vehículo enciende? si
¿El vehículo hace ruidos extraños? si
¿Dónde se escucha el ruido? frenos
```

**Salida del sistema:**
```
 DIAGNÓSTICO: Problema en los FRENOS
   - Posibles causas: pastillas gastadas, discos desgastados
   - Recomendación: ¡URGENTE! Revisar sistema de frenos inmediatamente
```

---

### Caso 3: Alto Consumo de Combustible

**Entrada del usuario:**
```
¿El vehículo enciende? si
¿El vehículo hace ruidos extraños? no
¿Tiene problemas de rendimiento? si
¿Qué problema presenta? consumo
```

**Salida del sistema:**
```
 DIAGNÓSTICO: ALTO CONSUMO de combustible
   - Posibles causas: filtro de aire sucio, inyectores, presión de neumáticos
   - Recomendación: Revisar filtros y sistema de inyección
```

---

## Análisis del Sistema

###  Ventajas

- **Facilidad de uso**: El sistema guía al usuario mediante preguntas simples
- **Diagnóstico estructurado**: Sigue un árbol de decisión lógico
- **Recomendaciones claras**: Proporciona acciones específicas a tomar
- **Escalabilidad**: Fácil de expandir con más reglas y diagnósticos

### Limitaciones

- No considera múltiples problemas simultáneos
- Requiere que el usuario identifique correctamente los síntomas
- No sustituye un diagnóstico profesional
- Limitado a problemas comunes predefinidos

---

## Conclusiones

El sistema de diagnóstico implementado demuestra la efectividad de los sistemas basados en reglas para:

- Realizar diagnósticos sistemáticos mediante preguntas guiadas
- Proporcionar recomendaciones específicas según los síntomas
- Facilitar la identificación de problemas comunes en vehículos
- Aplicar lógica condicional de manera estructurada

El sistema puede expandirse agregando más reglas y casos específicos para mejorar la precisión del diagnóstico.


## Referencias

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach*. Pearson.
- Documentación oficial de Python 3: https://docs.python.org/3/
- Giarratano, J., & Riley, G. (2004). *Expert Systems: Principles and Programming*. PWS Publishing.

---


** Si te ha sido útil, no olvides dar una estrella al repositorio!**
