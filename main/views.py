from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import ImagePair,Article,Devi,AvisUtilisateur,Video,Contact
from django.contrib import messages
from django.http import JsonResponse
from .forms import VideoForm

# Create your views here.
# Create your views here.
def recuperer_commentaires():
    return AvisUtilisateur.objects.all()

def index(request):
    image_pairs = ImagePair.objects.all()
    commentaires = recuperer_commentaires()
    videos = Video.objects.all()  # Ajoutez cette ligne pour récupérer les vidéos
    return render(request, 'main/index.html', {'image_pairs': image_pairs, 'commentaires': commentaires, 'videos': videos})

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VideoForm()
    return render(request, 'main/add_video.html', {'form': form})


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})


def devis(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        telephone = request.POST.get('telephone')
        prestation_id = request.POST.get('prestation_id')
        observation = request.POST.get('observation')

        # Enregistrez les données dans la base de données
        devis = Devi(
            type=type,
            name=name,
            email=email,
            address=address,
            telephone=telephone,
            prestation_id=prestation_id,
            observation=observation
        )
        devis.save()

        # Affichez un message flash de succès
        messages.success(request, 'Devis soumis avec succès.')

    return render(request,'main/devis.html')

    
def traiter_avis(request):
    if request.method == 'POST':
        commentaire = request.POST.get('commentaire')
        nouvel_avis = AvisUtilisateur(commentaire=commentaire)
        nouvel_avis.save()
        commentaires = recuperer_commentaires()
        return JsonResponse({'commentaires': list(commentaires.values())})
    else:
        return HttpResponse("Méthode non autorisée")
    

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/article_detail.html', {'article': article})


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('Message')  # Utilisation du bon nom de champ
        contact = Contact(email=email, message=message)
        contact.save()

        # Ajoutez un message de réussite
        messages.success(request, 'Le formulaire a été envoyé avec succès.')

        return HttpResponseRedirect(request.path_info)  # Redirection vers la même page

    return render(request, 'main/contact.html')
