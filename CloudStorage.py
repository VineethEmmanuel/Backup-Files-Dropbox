import dropbox

class UploadData:
    def __init__(self, token):
        self.token = token

    def upload_file(self, src, dest):
        dbx = dropbox.Dropbox(self.token)

        f = open(src, 'rb')

        dbx.files_upload(f.read(), dest)

def main():
    token = "sl.A0KSaynUb04Znk5pL63OKquzn8wWNttt0pfKucnqXMpMgbmulV6k7fsZedNfzvsbQPJi_AwV9O0P72Y5ag4H1b2Cf1auYuS9bNs7ZFA1pzBzEU7H5xi5jYRSAD1QtC0ljnQOMT4g"
    uploadData = UploadData(token)

    src = input('Enter the File Path: ')
    dest = input('Enter the Destination File Path: ')

    uploadData.upload_file(src, dest)
    print('Your Files Have Been Moved to Dropbox Successfully')

if __name__ == '__main__':
    main()