import os
import http.server
from time import *
from sys import *


def clear():
	os.system('clear')

site_statique_logo = r'''
< site-statique >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
site_statique_prompt = "site-statique ~# "

class site_statique():
	def __init__(self):
		os.system('mode con: cols=80 lines=25')
		clear()
		print(site_statique_logo + r'''
[!]----------Coded by Lucas Mouchague----------[!]''' + r'''


{1}--- Définir le chemin du dossier ---
{2}--- Convertir le fichier markdown en html ---
{3}--- Demarrer le serveur web ---
					''')

		choice = input(site_statique_prompt)
		if choice == "1":
			menu_chemin_dossier()
		if choice == "2":
			menu_conversion()		
		if choice == "3":
			menu_serveur()


class menu_chemin_dossier:
	logo_menu_chemin_dossier = r'''
[!] ---------- Définir le chemin du dossier ---------- [!]'''
	def __init__(self):
		clear()
		print(self.logo_menu_chemin_dossier)
		print(r''' 

{1}--- Choisir le chemin du fichier a convertir ---
{99}--- Retour au menu ---
			''')
		choice_chemin_dossier = input(site_statique_prompt)
		if choice_chemin_dossier == "1":
			clear()
			print(r''' 
[!] --- Choisir le chemin du fichier a convertir --- [!]
				''')
			chemin = input(site_statique_prompt)
			if chemin != "":
				site_statique()
		if choice_chemin_dossier == "99":
			site_statique()
class menu_conversion:
	logo_menu_conversion = r'''
[!] ---------- Convertir le fichier markdown en html ---------- [!] '''
	def __init__(self):
	 	clear()
	 	print(self.logo_menu_conversion)
	 	print(r''' 
{1}--- Convertir le fichier ---
{99}--- Retour au menu ---
	 		''')
	 	choice_menu_conversion = input(site_statique_prompt)
	 	if choice_menu_conversion == "1":
	 		pass
 		if choice_menu_conversion == "99":
 			site_statique()

class menu_serveur:
	logo_menu_serveur = r'''
[!] ---------- Demarrer le serveur web ---------- [!]'''
	def __init__(self):
		clear()
		print(self.logo_menu_serveur)
		print(r'''

{1}--- definir l'ip du serveur web (par défaut: 127.0.0.1) ---
{2}--- definir le port du serveur web (par défaut: 8080) ---
{3}--- demarrer le serveur web ---
{4}--- Stopper le serveur web ---
{99}--- Retour au menu ---
			''')
		choice_menu_serveur = input(site_statique_prompt)
		if choice_menu_serveur == "1":
			clear()
			print(r'''
[!] --- definir l'ip du serveur web (par défaut: 127.0.0.1) --- [!]
				''')


			ip_defini = input(site_statique_prompt)
			
			if ip_defini != "":
				menu_serveur()
		
		if choice_menu_serveur == "2":
			clear()
			print(r'''
[!] --- definir le port du serveur web (par défaut: 8080) --- [!]
				''')


			port_defini = input(site_statique_prompt)

			if port_defini != int():
				print (port_defini)
				menu_serveur()

		if choice_menu_serveur == "3":
			if ip_defini == "" and port_defini == int():
				start_serveur("127.0.0.1", 8080)
			else:
				start_serveur(ip_defini, port_defini)
			print("server started")
			#site_statique()
		
		if choice_menu_serveur == "4":
			pass
		
		if choice_menu_serveur == "99":
			site_statique()


def start_serveur(ip_defini, port_defini):

	port = port_defini
	host = ip_defini

	serveur_adresse = (host, port)
	serveur = http.server.HTTPServer
	
	handler = http.server.CGIHTTPRequestHandler
	handler.cgi_directories = [chemin]

	httpd = serveur(serveur_adresse, handler)
	httpd.serve_forever()

def stop_serveur():
	pass

if __name__ == "__main__":
	try:
		site_statique()
	except KeyboardInterrupt:
		print("Closing program...\n")
		time.sleep(1)