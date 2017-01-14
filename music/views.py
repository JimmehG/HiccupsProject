from django.shortcuts import render

# Create your views here.


links = {
	'bliss': '237926802?secret_token=s-EMXY7',
	'bourgeois': '284677312?secret_token=s-l9A1U',
	'cigarette': '294856703?secret_token=s-WylxL',
	'spacecadet': '292054339?secret_token=s-ERfRh',
	'waterfall': '275717056',
	'complexion': '275719279',
	'noisecancelling': '295678494?secret_token=s-DQW4q',
	'deadlines': '288804429',
	'databug': '295818925?secret_token=s-l30oK',
}
colours = {
	'bliss': '25ab30',
	'bourgeois': 'eef431',
	'cigarette': 'a16e96',
	'spacecadet': '0066cc',
	'waterfall': '00d1e6',
	'complexion': 'ed1137',
	'noisecancelling': 'FFFFFF',
	'deadlines': '000000',
	'databug': '000000',
}


def index(request):
	return render(request, 'index.html')


def bliss(request):
	name = 'bliss'
	context = get_basic_context(name)
	return music_page(request, context)


def spacecadet(request):
	name = 'spacecadet'
	context = get_basic_context(name)
	return music_page(request, context)


def bourgeois(request):
	name = 'bourgeois'
	context = get_basic_context(name)
	return music_page(request, context)


def cigarette(request):
	name = 'cigarette'
	context = get_basic_context(name)
	return music_page(request, context)


def complexion(request):
	name = 'complexion'
	context = get_basic_context(name)
	return music_page(request, context)


def noisecancelling(request):
	name = 'noisecancelling'
	context = get_basic_context(name)
	return music_page(request, context)


def databug(request):
	name = 'databug'
	context = get_basic_context(name)
	return music_page(request, context)


def deadlines(request):
	name = 'deadlines'
	context = get_basic_context(name, '.png')
	return music_page(request, context)


def waterfall(request):
	name = 'waterfall'
	context = get_basic_context(name)
	context['title'] = 'islands【ᴡᴀᴛᴇʀғᴀʟʟ】'
	return music_page(request, context)


def get_basic_context(name, extension='.jpg'):
	return {
		'page_body_name': 'views/' + name + '.html',
		'link': links[name],
		'colour': colours[name],
		'name': name,
		'image_name': 'images/' + name + extension,
		'show_user': 'true',
		'title': name
	}


def music_page(request, context):
	return render(request, 'music page.html', context)
