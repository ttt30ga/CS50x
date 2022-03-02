// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10000;

// Hash table
node *table[N];

// Word counter, to use in Size function
int word_counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash word
    int hash_word = hash(word);

    // Index linked list
    node *cursor = table[hash_word];

    // Traverse linked list
    while (cursor != NULL)
    {
        // Check if cursor.word match word
        // '== 0' check if they are equal
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        // Got to next word
        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int sum = 0;

    // Loop through the lenght of the word
    for (int i = 0; i < strlen(word); i ++)
    {
        // Sum the ASCII value of each letter of athe word
        sum += tolower(word[i]);
    }

    // Keep the value in range
    int val = sum % N;

    return val;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary file and check if opened
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not open file\n");
        return false;
    }
    else
    {
        // Create a variable for word
        char word[LENGTH + 1];

        // Loop through word in file
        while (fscanf(file, "%s", word) != EOF)
        {
            // Create a node for each word
            node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                unload();
                return false;
            }

            // Copy word into node unless is NULL
            strcpy(n->word, word);
            n->next = NULL;

            // Use hash function
            int head = hash(word);

            // Insert node into hash table
            n->next = table[head];
            table[head] = n;

            word_counter++;
        }
    }
    // Close file
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return word_counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Loop through N
    for (int i = 0; i < N; i++)
    {
        // Create pointers
        node *head = table[i];
        node *cursor = head;
        node *tmp = cursor;

        while (cursor != NULL)
        {
            // Until cursor is equal to NULL go to the next cursor
            cursor = cursor->next;
            // Free temporary pointer
            free(tmp);
            // Move temporary pointer to cursor
            tmp = cursor;
        }
    }
    return true;
}
