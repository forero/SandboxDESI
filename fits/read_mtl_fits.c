/* 
   Example code for merged-target-list MTL files.
*/

#include <stdlib.h>
#include <string.h>
#include "fitsio.h"

int main(int argc, char**argv){
  char filename[512];
char card[FLEN_CARD]; 
 char keyname[FLEN_KEYWORD], colname[FLEN_VALUE], coltype[FLEN_VALUE];
 int ii;
 int nkeys;
 int hdupos;
 int hdutype;
 int ncols;
 int colnum;
 long naxes[10], nrows;
  strcpy(filename, argv[1]);
  printf("reading %s\n", filename);

  long *targetid;
  int *numobs;
  int *priority;
  float *ra;
  float *dec;

  fitsfile *fptr;        
  int status = 0, anynulls;

  if (!  fits_open_file(&fptr, filename, READONLY, &status)){
    /* move to the last (2rd) HDU in the output file */
    if ( fits_movabs_hdu(fptr, 2, &hdutype, &status) )
      exit(status);
    

    fits_get_hdrspace(fptr, &nkeys, NULL, &status);
    
    
    fits_get_hdu_num(fptr, &hdupos);
    fits_get_hdu_type(fptr, &hdutype, &status);  /* Get the HDU type */
    
    
    fits_get_num_rows(fptr, &nrows, &status);
    fits_get_num_cols(fptr, &ncols, &status);
    
    printf("\nHDU #%d  ", hdupos);
    if (hdutype == ASCII_TBL)
      printf("ASCII Table:  ");
    else
      printf("Binary Table:  ");
    
    
    printf("%d columns x %ld rows\n", ncols, nrows);
    printf(" COL NAME             FORMAT\n");
    for (ii = 1; ii <= ncols; ii++)
      {
	fits_make_keyn("TTYPE", ii, keyname, &status); /* make keyword */
	fits_read_key(fptr, TSTRING, keyname, colname, NULL, &status);
	fits_make_keyn("TFORM", ii, keyname, &status); /* make keyword */
	fits_read_key(fptr, TSTRING, keyname, coltype, NULL, &status);	
	printf(" %3d %-16s %-16s\n", ii, colname, coltype);
      }
  }

  if(!(targetid=malloc(nrows * sizeof(long)))){
    fprintf(stderr, "problem with targetid allocation\n");
    exit(1);
  }
  if(!(numobs=malloc(nrows * sizeof(int)))){
    fprintf(stderr, "problem with targetid allocation\n");
    exit(1);
  }
  if(!(priority=malloc(nrows * sizeof(int)))){
    fprintf(stderr, "problem with targetid allocation\n");
    exit(1);
  }
  if(!(ra=malloc(nrows * sizeof(float)))){
    fprintf(stderr, "problem with targetid allocation\n");
    exit(1);
  }

  if(!(dec=malloc(nrows * sizeof(float)))){
    fprintf(stderr, "problem with targetid allocation\n");
    exit(1);
  }

/* find which column contains the TARGETID values */
  if ( fits_get_colnum(fptr, CASEINSEN, "TARGETID", &colnum, &status) ){
    fprintf(stderr, "error\n");
    exit(status);
  }

  long frow, felem, nullval;
  frow = 1;
  felem = 1;
  nullval = -99.;
  if (fits_read_col(fptr, TLONG, colnum, frow, felem, nrows, 
		    &nullval, targetid, &anynulls, &status) ){
    fprintf(stderr, "error\n");
    exit(status);
  }

  if ( fits_get_colnum(fptr, CASEINSEN, "RA", &colnum, &status) ){
    fprintf(stderr, "error\n");
    exit(status);
  }
 if (fits_read_col(fptr, TFLOAT, colnum, frow, felem, nrows, 
		    &nullval, ra, &anynulls, &status) ){
    fprintf(stderr, "error\n");
    exit(status);
  }


  int i;
  for(i=0;i<10;i++){
    fprintf(stdout, "TARGETID %ld\n", targetid[i]);
  }
  for(i=nrows-10;i<nrows;i++){
    fprintf(stdout, "TARGETID %ld\n", targetid[i]);
  }

  return(status);
}
