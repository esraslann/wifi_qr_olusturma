import qrcode

def create_wifi_qr(ssid, password, encryption_type="WPA"):
    # WiFi bilgilerini formatla
    wifi_string = f"WIFI:T:{encryption_type};S:{ssid};P:{password};;"
    
    # QR kodunu oluştur
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(wifi_string)
    qr.make(fit=True)
    
    # QR kodunu görsel olarak oluştur
    img = qr.make_image(fill='black', back_color='white')
    
    # Görseli kaydet
    img.save(f"{ssid}_wifi_qr.png")
    print(f"WiFi QR kodu {ssid}_wifi_qr.png olarak kaydedildi.")

# WiFi bilgilerinizi buraya girin
ssid = "wifi isminizi yazın"
password = "wifi şifresini yazın"
encryption_type = "WPA2"  # WPA, WPA2, veya WPA3 kullanabilirsiniz

create_wifi_qr(ssid, password, encryption_type)
