<!DOCTYPE html>
<head>
</head>

<body>
    <h1>CyberSentinel</h1>
    <p>CyberSentinel es un script de Python que monitorea URLhaus, detecta nuevas amenazas y envía alertas por correo electrónico utilizando la API de SendGrid.</p>
    <h2>Requisitos</h2>
    <ul>
        <li>Python 3.6+</li>
        <li>Bibliotecas: <code>requests</code>, <code>sendgrid</code></li>
        <li>Cuenta en SendGrid con una clave API</li>
    </ul>
    <h2>Instalación</h2>
    <ol>
        <li>Clone el repositorio:</li>
        <pre><code>git clone https://github.com/ManuAP/CiberSentinel
cd cybersentinel
        </code></pre>
        <li>Instale las dependencias:</li>
        <pre><code>pip install -r requirements.txt
        </code></pre>
        <li>Configure las variables de entorno:</li>
        <ul>
            <li><code>SENDGRID_API_KEY</code>: La clave API de SendGrid.</li>
            <li><code>YOUR_EMAIL_ADDRESS</code>: La dirección de correo electrónico del remitente.</li>
            <li><code>RECIPIENT_EMAIL_ADDRESS</code>: La dirección de correo electrónico del destinatario.</li>
        </ul>
        <p>Puede hacerlo agregando las siguientes líneas a su archivo <code>.bashrc</code>, <code>.zshrc</code> u otro archivo de configuración de shell:</p>
        <pre><code>export SENDGRID_API_KEY='your_sendgrid_api_key'
export YOUR_EMAIL_ADDRESS='your_email_address'
export RECIPIENT_EMAIL_ADDRESS='recipient_email_address'
        </code></pre>
        <p>No olvide reemplazar <code>your_sendgrid_api_key</code>, <code>your_email_address</code> y <code>recipient_email_address</code> con sus propios valores.</p>
        <li>Ejecute el script:</li>
        <pre><code>python CyberSentinel.py
        </code></pre>
        <p>El script comenzará a monitorear URLhaus y enviará un correo electrónico cada vez que detecte una nueva amenaza.</p>
    </ol>
</body>
</html>
