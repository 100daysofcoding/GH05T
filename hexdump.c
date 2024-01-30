#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 16

void hex_dump(const void* data, size_t size) {
    unsigned char* ptr = (unsigned char*)data;
    size_t i, j;

    for (i = 0; i < size; i += BUFFER_SIZE) {
        printf("%08lx: ", (unsigned long)(ptr + i));

        for (j = 0; j < BUFFER_SIZE; j++) {
            if (i + j < size) {
                printf("%02x ", ptr[i + j]);
            } else {
                printf("   ");
            }

            if (j % 8 == 7) {
                printf(" ");
            }
        }

        printf(" ");
        for (j = 0; j < BUFFER_SIZE && i + j < size; j++) {
            if (ptr[i + j] >= 32 && ptr[i + j] <= 126) {
                printf("%c", ptr[i + j]);
            } else {
                printf(".");
            }
        }

        printf("\n");
    }
}

int main() {
    // Exemple d'utilisation : hexdump du code ASCII de "Hello, World!"
    const char* message = "Hello, World!";
    size_t message_size = strlen(message);

    hex_dump(message, message_size);

    return 0;
}
