import ftp

ftp = ftplib.FTP( 'sidads.colorado.edu' )
ftp.cwd( '/pub/DATASETS/nsidc0051_gsfc_nasateam_seaice/final-gsfc/north/monthly' )


numpy.fromfile(f, dtype=np.int8)


path = 'ftp://sidads.colorado.edu/pub/DATASETS/nsidc0051_gsfc_nasateam_seaice/final-gsfc/north/monthly'


import urllib2

path = 'ftp://sidads.colorado.edu/pub/DATASETS/nsidc0051_gsfc_nasateam_seaice/final-gsfc/north/monthly'

req = urllib2.Request( path )

response = urllib2.urlopen( req )

page = response.read()
filelist = page.splitlines()

filenames = [ f.split()[len(f.split())-1] for f in filelist ]

splitter =[ filenames.split( '_' ) for f in filenames ]

def get_date( f ):
	f = f.split()[len(f.split())-1]
	split = f.split( '_' )
	split = split[1]
	return( f, split )



