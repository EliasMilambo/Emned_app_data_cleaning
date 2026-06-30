import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def prototype_data_cleaner(request):
    if request.method == "POST" and request.FILES.get('fichier_excel'):
        fichier = request.FILES['fichier_excel']

        try:
            # 1. Pandas lit le fichier (Excel ou CSV) envoyé par l'utilisateur
            if fichier.name.endswith('.csv'):
                df = pd.read_csv(fichier)
            else:
                df = pd.read_excel(fichier)

            # 2. Nettoyage de base avec vos 50% de maîtrise Pandas
            df.drop_duplicates(inplace=True)  # Supprime les doublons
            df.dropna(how='all', inplace=True)  # Supprime les lignes totalement vides

            # 3. Préparation du fichier nettoyé pour le renvoyer au client
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="excel_nettoye_emned.xlsx"'

            # Sauvegarde du résultat dans la réponse
            df.to_excel(response, index=False)
            return response
            messages.success(request, f"Bravo, fichier traiter avec succes !")

            return redirect('data:data_cleaner')


        except Exception as e:
            messages.error(request, f"Erreur lors du traitement : {str(e)}")

    return render(request, 'data_cleaner.html')
