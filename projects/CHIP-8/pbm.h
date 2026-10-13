#pragma once
#include <stdlib.h>
#include <stdio.h>

typedef struct {
    unsigned int ** pixmap; //h x w (2-dimensional) bitmap array
    unsigned int height, width;
} PBMImage;

PBMImage * new_pbmimage(unsigned int w, unsigned int h)
{
    PBMImage* img = (PBMImage*)malloc(sizeof(PBMImage));
    img->pixmap = (unsigned int**)malloc(sizeof(unsigned int) * h);
    for (unsigned int i = 0; i < h; i++) {
        img->pixmap[i] = (unsigned int*)malloc(sizeof(unsigned int) * w);
    }
    img->height = h;
    img->width = w;
    return img;
}

void write_pbmfile( PBMImage *pbm, const char * filename ) {
    FILE * outfile;
    
    if( (outfile = fopen( filename, "w" )) == NULL ) {
        perror("fopen()");
        exit( -1 );
     }

    //write pbm header
    fprintf(outfile, "P1\n%d %d\n", pbm->width, pbm->height);
    
    //write pbm pixmap
    for( int h=0; h<pbm->height; h++ ){
        for ( int w=0; w<pbm->width; w++ ){
            fprintf(outfile, "%d ", pbm->pixmap[h][w] );
        }
            
        fprintf(outfile, "\n"); //newline after each row
    }
    
    fclose( outfile );
}