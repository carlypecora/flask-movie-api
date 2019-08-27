from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():
	movie_data = request.get_json()

	return 'Done', 201

@main.route('/movies')
def movies():

	movies = []

	return jsonify({'movies' : movies})