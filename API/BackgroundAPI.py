from flask import Flask, jsonify
from BackgroundsJSON import backgrounds

app = Flask(__name__)


@app.route("/backgrounds", methods=["GET"])
def get_backgrounds():
    return jsonify(backgrounds)


@app.route("/background/<background_name>", methods=["GET"])
def get_background(background_name):
    if background_name == "acolyte":
        return jsonify(backgrounds["results"][0])
    elif background_name == "charlatan":
        return jsonify(backgrounds["results"][1])
    elif background_name == "criminal":
        return jsonify(backgrounds["results"][2])
    elif background_name == "entertainer":
        return jsonify(backgrounds["results"][3])
    elif background_name == "folk-hero":
        return jsonify(backgrounds["results"][4])
    elif background_name == "guild-artisan":
        return jsonify(backgrounds["results"][5])
    elif background_name == "hermit":
        return jsonify(backgrounds["results"][6])
    elif background_name == "noble":
        return jsonify(backgrounds["results"][7])
    elif background_name == "outlander":
        return jsonify(backgrounds["results"][8])
    elif background_name == "sage":
        return jsonify(backgrounds["results"][9])
    elif background_name == "sailor":
        return jsonify(backgrounds["results"][10])
    elif background_name == "soldier":
        return jsonify(backgrounds["results"][11])
    else:
        return jsonify({"Error": "Background Not Found!!!"})

# Run app
if __name__ == "__main__":
    app.run(debug=False)
