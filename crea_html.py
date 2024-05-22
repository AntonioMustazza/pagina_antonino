html_content = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagina di Antonino Mustazza</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #ffffff;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #f0f8ff;
            padding: 20px;
            display: flex;
            align-items: center;
            border-bottom: 2px solid #d3d3d3;
        }
        .profile-image {
            border-radius: 50%;
            width: 140.5px;
            height: 140.5px;
            margin-right: 20px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .profile-image:hover {
            transform: scale(1.1);
        }
        .profile-name {
            font-size: 50px; /* Incrementato del 25% */
            font-weight: bold;
        }
        nav {
            margin-left: auto;
            display: flex;
            align-items: center;
        }
        nav a {
            margin: 0 15px;
            text-decoration: none;
            color: #333;
            font-size: 22px;
            display: flex;
            align-items: center;
        }
        nav img {
            width: 40px;
            height: 26px;
            margin-right: 6px;
        }
        .container {
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        .quote {
            text-align: center;
            font-size: 24px;
            font-style: italic;
            color: #555;
            margin: 20px 0;
            padding: 0 20px;
        }
        .cv-section {
            margin-top: 40px;
            margin-bottom: 40px;
            padding: 20px;
            background-color: #f9f9f9;
            border: 2px solid #d3d3d3;
            border-radius: 15px;
            text-align: center;
        }
        .cv-section a {
            color: #d4af37;
            text-decoration: none;
            font-weight: bold;
        }
        .cv-section a:hover {
            color: #b8860b; /* Giallo più intenso */
        }
        .post-section {
            text-align: center;
        }
        .post-section h2 {
            font-size: 28px;
            margin-bottom: 20px;
        }
        .post {
            border: 2px solid #d3d3d3;
            border-radius: 5px;
            margin-bottom: 20px;
            padding: 10px;
            background-color: #f9f9f9;
            text-align: center;
        }
        .post img {
            max-width: 50%; /* Ridotto del 50% */
            border-radius: 4px;
            cursor: pointer;
        }
        .button {
            background-color: #b8860b; /* Giallo più intenso */
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 10px;
            font-size: 16px;
            color: #fff;
        }
        .button:hover {
            background-color: #996515;
        }
        footer {
            background-color: #f0f8ff;
            padding: 10px;
            text-align: center;
            margin-top: 20px;
            border-top: 2px solid #d3d3d3;
        }
        footer a {
            text-decoration: none;
            color: #333;
            font-size: 18px;
            margin: 0 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        footer img {
            width: 30px;
            height: 18px;
            margin-right: 5px;
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgb(0,0,0);
            background-color: rgba(0,0,0,0.9);
        }
        .modal-content {
            margin: auto;
            display: block;
            width: 80%;
            max-width: 700px;
        }
        .modal-content {  
            animation-name: zoom;
            animation-duration: 0.6s;
        }
        @keyframes zoom {
            from {transform: scale(0)} 
            to {transform: scale(1)}
        }
        .close {
            position: absolute;
            top: 15px;
            right: 35px;
            color: #fff;
            font-size: 40px;
            font-weight: bold;
            transition: 0.3s;
        }
        .close:hover,
        .close:focus {
            color: #bbb;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header>
        <img src="tuo_profilo.jpg" alt="Immagine Profilo" class="profile-image" id="profilePic">
        <div class="profile-name">Antonino Mustazza</div>
        <nav>
            <a href="https://www.instagram.com/sickily_">
                <img src="instagram_logo.png" alt="Instagram"> Instagram
            </a>
            <a href="https://x.com/musty_eu">
                <img src="twitter_logo.png" alt="Twitter"> Twitter
            </a>
            <a href="https://www.linkedin.com/in/a-must/">
                <img src="linkedin_logo.png" alt="LinkedIn"> LinkedIn
            </a>
        </nav>
    </header>
    <div class="container">
        <div class="quote">
            "There's no guarantee that good ideas prevail. But if you don't try to have those good ideas and get them out there, then of course they won't prevail!" - Paul Krugman
        </div>
        <div class="cv-section">
            <h3><a href="CV_Antonino.pdf" target="_blank">Curriculum Vitae</a></h3>
        </div>
        <div class="post-section">
            <h2>Post di Instagram</h2>
            <div class="post">
                <a href="https://www.instagram.com/p/C5JrozXINKN/" target="_blank">
                    <img src="post_instagram_1.png" alt="Post di Instagram 1">
                </a>
                <p> Post di Instagram 1</p>
            </div>
            <div class="post">
                <a href="https://www.instagram.com/p/C6TgXt4IxiF/" target="_blank">
                    <img src="post_instagram_2.png" alt="Post di Instagram 2">
                </a>
                <p>Post di Instagram 2</p>
            </div>
        </div>
    </div>
    <footer>
        <p>© 2024 Antonio. Tutti i diritti riservati.</p>
        <a href="https://www.instagram.com/sickily_">
            <img src="instagram_logo.png" alt="Instagram"> Instagram
        </a>
        <a href="https://x.com/musty_eu">
            <img src="twitter_logo.png" alt="Twitter"> Twitter
        </a>
        <a href="https://www.linkedin.com/in/a-must/">
            <img src="linkedin_logo.png" alt="LinkedIn"> LinkedIn
        </a>
    </footer>
    <div id="myModal" class="modal">
        <span class="close">&times;</span>
        <img class="modal-content" id="img01">
    </div>
    <script>
        var modal = document.getElementById('myModal');
        var img = document.getElementById('profilePic');
        var modalImg = document.getElementById("img01");
        img.onclick = function(){
            modal.style.display = "block";
            modalImg.src = this.src;
        }
        var span = document.getElementsByClassName("close")[0];
        span.onclick = function() { 
            modal.style.display = "none";
        }
    </script>
</body>
</html>
"""

import os 
project_dir = 'C:/Users/anton/Documents/SICKILY/pagina_antonio'

# Crea la directory del progetto
os.makedirs(project_dir, exist_ok=True)

# Percorso del file HTML
html_file_path = os.path.join(project_dir, 'index.html')

# Scrivi il contenuto HTML nel file
with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"Pagina web creata con successo! File salvato in: {html_file_path}")


