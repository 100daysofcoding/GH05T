#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <arpa/inet.h>

void enumerate_subdomains(const char *domain) {
    struct hostent *h;
    int i;

    // Interroger le DNS pour obtenir les adresses IP associées au domaine
    if ((h = gethostbyname(domain)) == NULL) {
        herror("gethostbyname");
        return;
    }

    printf("Liste des adresses IP pour le domaine %s :\n", domain);
    for (i = 0; h->h_addr_list[i] != NULL; i++) {
        printf("%s\n", inet_ntoa(*(struct in_addr *)(h->h_addr_list[i])));
    }
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <domain>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    char *domain = argv[1];
    enumerate_subdomains(domain);

    return 0;
}
