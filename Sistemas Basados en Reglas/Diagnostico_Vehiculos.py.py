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
            print("\n DIAGNÓSTICO: El vehículo está en BUEN ESTADO")
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
            print("   - Posibles causas: batería agotada, terminales flojos/corroídos")
            print("   - Recomendación: Revisar conexiones de batería y estado de carga")

print("\n" + "=" * 50)
print("¡Gracias por usar el sistema de diagnóstico!")
print("Recuerde: Este es un diagnóstico preliminar.")
print("Siempre consulte con un mecánico profesional.")
print("=" * 50)