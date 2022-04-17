from re import template
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import FormView, DetailView
from .models import Place, Feedback
from .forms import PlaceForm, FeedbackForm
#from django.shortcuts import get_list_or_404

# Create your views here.

def places(request):
    place_objects = Place.objects.all()
    return render(request, 'places/places.html', {'places': place_objects})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def create_place(request):
    if request.method == "POST":
        place_form = PlaceForm(request.POST)
        if place_form.is_valid():
            place_form.save()
            return redirect(places)

    place_form = PlaceForm()
    return render(request, 'form.html', {'place_form': place_form})


def place(request, id):
    try:
        place_object = Place.objects.get(id=id)
        return render(request, 'place.html', {'place_object': place_object})
    except Place.DoesNotExist as e:
        return HttpResponse(f'Not found: {e}', status=404)

def edit_place(request, id):
    place_object = Place.objects.get(id=id)

    if request.method == "POST":
        place_form = PlaceForm(data=request.POST, instance=place_object)
        if place_form.is_valid():
            place_form.save()
            return redirect(place, id=id)

    place_form = PlaceForm(instance=place_object)
    return render(request, 'form.html', {'place_form': place_form})


#def delete_place(request, id):
#    place_object = Place.objects.get(id=id)
#    place.object.delete()
#    return redirect(places) 

def delete_place(request, id):
    Place.objects.filter(id=id).delete()
    return redirect('/places/')

#SomeModel.objects.filter(id=id).delete()
#instance = SomeModel.objects.get(id=id)
#instance.delete()

class FeedbackView(FormView):
    template_name = 'feedback_form.html'
    form_class = FeedbackForm
    success_url = '/places/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class FeedbackDetailView(DetailView):
    queryset = Feedback.objects.all()
    template_name = 'feedback.html'

#class FeedbackDetailView(generic.DetailView):
#    object = POST
#    template_name = 'places/feedback.html'

#    def get_object(self, queryset=None):
#        return get_list_or_404(Feedback, pk=self.kwargs.get('pk'))
