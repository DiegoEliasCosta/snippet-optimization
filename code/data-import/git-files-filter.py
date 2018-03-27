import pandas as pd
import os
import argparse


def filterFiles(dir, file_ext):
    ext = "." + file_ext
    filtered_files = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in [f for f in filenames if f.endswith(ext)]:
            filtered_files.append(os.path.join(dirpath, filename))

    return filtered_files


def filterAPIRelatedFiles(files_list, api_list):

    df = pd.DataFrame(columns=['File'])

    for file in files_list:
        try:
            with open(file, 'r', encoding="utf-8") as handler:
                lines = handler.readlines()
                for api in api_list:
                    for l in lines:
                        if 'import %s' % api in l:
                            df.loc[len(df)] = file
                            break
                        elif 'from %s' % api in l:
                            df.loc[len(df)] = file
                            break

        except UnicodeDecodeError as e:
            print('Error while reading = %s | %s' % (file, str(e)))

    return df


def readable_dir(prospective_dir):
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
    if os.access(prospective_dir, os.R_OK):
        return prospective_dir
    else:
        raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Filter files that import a specific API.')

    parser.add_argument('folder', type=readable_dir, help='parent folder where the files will be filtered')
    parser.add_argument('ext', type=str, help='target file extension (without `.`)')
    parser.add_argument('output', type=argparse.FileType('w'), help='file to output the paths without extension')

    parser.add_argument('--debug', help='output in adittion a csv file')
    parser.add_argument('--api', type=str, nargs='+', help='list of api names to search for')

    args = parser.parse_args()

    files = filterFiles(args.folder, args.ext)
    print('Total of %d files found with the extension %s' % (len(files), args.ext))

    files_df = filterAPIRelatedFiles(files, args.api)
    print('Total of %d files found with at least ONE of the libraries %s' % (len(files_df), args.api))

    files_df.to_pickle(args.output.name)
    if args.debug:
        files_df.to_csv(args.output.name + '.csv')

    print('Files path successfully stored in %s' % args.output.name)
