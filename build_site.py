import os

def build_site():
    # Maak folder site aan als die niet bestaat
    if not os.path.exists("site"):
        os.mkdir("site")

    # Basis HTML content
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mijn Portfolio</title>
    </head>
    <body>
        <h1>Welkom op mijn portfolio</h1>
        <p>Dit is een simpele website die ik zelf met Python maak.</p>
    </body>
    </html>
    """

    # Schrijf naar index.html in site folder
    with open("site/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Website is gebouwd in de folder 'site'!")

if __name__ == "__main__":
    build_site()
