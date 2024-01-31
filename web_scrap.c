#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

// Structure pour stocker les données de téléchargement
struct MemoryStruct {
    char *memory;
    size_t size;
};

// Fonction de rappel pour le traitement des données téléchargées
size_t WriteMemoryCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    struct MemoryStruct *mem = (struct MemoryStruct *)userp;

    mem->memory = realloc(mem->memory, mem->size + realsize + 1);

    if (mem->memory == NULL) {
        fprintf(stderr, "Erreur d'allocation de mémoire\n");
        return 0;
    }

    memcpy(&(mem->memory[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return realsize;
}

// Fonction pour télécharger une URL et stocker le contenu dans une structure MemoryStruct
CURLcode DownloadUrl(const char *url, struct MemoryStruct *chunk) {
    CURL *curl;
    CURLcode res;

    curl_global_init(CURL_GLOBAL_DEFAULT);

    curl = curl_easy_init();

    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);

        // Suivi des redirections
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

        // Définir la fonction de rappel pour traiter les données téléchargées
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)chunk);

        // Exécution de la requête
        res = curl_easy_perform(curl);

        // Gestion des erreurs
        if (res != CURLE_OK) {
            fprintf(stderr, "Erreur lors de la requête HTTP : %s\n", curl_easy_strerror(res));
        }

        // Libérer les ressources
        curl_easy_cleanup(curl);
    } else {
        fprintf(stderr, "Erreur lors de l'initialisation de cURL\n");
        return CURLE_FAILED_INIT;
    }

    curl_global_cleanup();

    return res;
}

int main(void) {
    CURLcode res;
    struct MemoryStruct chunk;
    chunk.memory = malloc(1);  // initialisation
    chunk.size = 0;

    const char *url = "https://example.com"; // Remplacez par l'URL du site à parcourir

    // Télécharger la page principale du site
    res = DownloadUrl(url, &chunk);

    if (res != CURLE_OK) {
        fprintf(stderr, "Échec du téléchargement de l'URL : %s\n", url);
        free(chunk.memory);
        return 1;
    }

    // Vous pouvez maintenant analyser le contenu de la page (chunk.memory)
    // et extraire les liens des images pour les télécharger à leur tour.

    printf("Contenu téléchargé : \n%s\n", chunk.memory);

    // Libérer la mémoire
    free(chunk.memory);

    return 0;
}
