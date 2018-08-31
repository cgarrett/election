from election import Election
import click

@click.command()
@click.option('--getcsv','-g',default=0,help='Gets the latest csv file.')
def main(getcsv):
	print('first stage cli')

	if getcsv==1:
		e = Election()
		e.get_file()
		e.extract_csv()
		e.delete_zip()


if __name__ == '__main__':
	main()