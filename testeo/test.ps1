# test.ps1 - Script de pruebas para Dante Propiedades Backend

Write-Host "🚀 INICIANDO PRUEBAS DEL BACKEND DANTE PROPIEDADES" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Yellow

# URL base del servidor
$BASE_URL = "http://127.0.0.1:8000"

# Función para hacer requests con formato
function Invoke-Test {
    param($Name, $Method, $Endpoint, $Body = $null)
    
    Write-Host "`n🧪 TEST: $Name" -ForegroundColor Cyan
    Write-Host "🔗 Endpoint: $Method $Endpoint" -ForegroundColor Gray
    
    try {
        $headers = @{
            "Content-Type" = "application/json"
        }
        
        if ($Body) {
            Write-Host "📦 Body: $Body" -ForegroundColor Gray
            $response = Invoke-RestMethod -Uri "$BASE_URL$Endpoint" -Method $Method -Headers $headers -Body $Body
        } else {
            $response = Invoke-RestMethod -Uri "$BASE_URL$Endpoint" -Method $Method -Headers $headers
        }
        
        Write-Host "✅ ÉXITO" -ForegroundColor Green
        $response | ConvertTo-Json -Depth 3
    }
    catch {
        Write-Host "❌ ERROR: $($_.Exception.Message)" -ForegroundColor Red
        if ($_.Exception.Response) {
            $stream = $_.Exception.Response.GetResponseStream()
            $reader = New-Object System.IO.StreamReader($stream)
            $reader.BaseStream.Position = 0
            $reader.DiscardBufferedData()
            $responseBody = $reader.ReadToEnd()
            Write-Host "📄 Respuesta del error: $responseBody" -ForegroundColor Red
        }
    }
}

# 1. Verificar estado del servidor
Write-Host "`n1️⃣ VERIFICANDO ESTADO DEL SERVICIO" -ForegroundColor Magenta
Invoke-Test -Name "Status Check" -Method GET -Endpoint "/status"

# 2. Página principal
Write-Host "`n2️⃣ PÁGINA PRINCIPAL" -ForegroundColor Magenta
Invoke-Test -Name "Root Endpoint" -Method GET -Endpoint "/"

# 3. Métricas
Write-Host "`n3️⃣ MÉTRICAS DEL SISTEMA" -ForegroundColor Magenta
Invoke-Test -Name "Metrics" -Method GET -Endpoint "/metrics"

# 4. Pruebas de chat
Write-Host "`n4️⃣ PRUEBAS DE CHAT" -ForegroundColor Magenta

# Consulta simple
$body_simple = '{"message": "Hola, ¿qué tipos de propiedades tienen?", "channel": "web"}'
Invoke-Test -Name "Chat Simple" -Method POST -Endpoint "/chat" -Body $body_simple

# Búsqueda con filtros
$body_busqueda = '{"message": "Busco departamento en alquiler en Palermo hasta 300000", "channel": "web"}'
Invoke-Test -Name "Chat con Búsqueda" -Method POST -Endpoint "/chat" -Body $body_busqueda

# Consulta WhatsApp
$body_whatsapp = '{"message": "Hola, quiero ver casas en venta", "channel": "whatsapp"}'
Invoke-Test -Name "Chat WhatsApp" -Method POST -Endpoint "/chat" -Body $body_whatsapp

# 5. Propiedades directas
Write-Host "`n5️⃣ BÚSQUEDA DIRECTA DE PROPIEDADES" -ForegroundColor Magenta
Invoke-Test -Name "Propiedades" -Method GET -Endpoint "/properties?neighborhood=Palermo&min_rooms=2"

# 6. Logs
Write-Host "`n6️⃣ REGISTROS DE CONVERSACIONES" -ForegroundColor Magenta
Invoke-Test -Name "Logs" -Method GET -Endpoint "/logs?limit=3"

# 7. Cache
Write-Host "`n7️⃣ GESTIÓN DE CACHE" -ForegroundColor Magenta
Invoke-Test -Name "Clear Cache" -Method DELETE -Endpoint "/cache"

Write-Host "`n🎯 TODAS LAS PRUEBAS COMPLETADAS" -ForegroundColor Green
Write-Host "📚 Para más pruebas, visita: $BASE_URL/docs" -ForegroundColor Yellow