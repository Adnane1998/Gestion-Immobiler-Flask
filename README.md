# Gestion-Immobiler-Flask

<h2>Choix technologiques :<br/></h2>
<hr>
Langage : Python<br/>
Framework : Flask<br/>
Base de données : Mysql<br/>
Test Api:PostMan
IDE:PyCharm<br/>
Serveur Web local :Xampp<br/>
Architecture MVC<br/>
Modéle:User,Good<br/>
Vue:JinJa<br/>

 <h2>Demarrer le projet:<br/></h2>
<hr>
 1)Créer une Base de donnée sur mysql(phpmyAdmin) : Immobilier
 2)Créer les tables en se dirignat vers le terminal: <br/>
   python <br/>
   from app import db <br/>
   db.create_all() <br/>
   exit() <br/>
   les tables seront créés <br/>
   3)Se diriger vers postman créer un  admin pour une méthode post sur l'url suivant: <br/>
    http://127.0.0.1:5000/insert_user pour champs: first_name,last_name,birth_date,type(admin),city <br/>
   
 4)<br/>
 docker build -t xxx <br/>
 docker run -it -p 5000:5000 xxxx.   <br/>
 Se diriger vers l'adresse http://127.0.0.1:5000/ (id de l'admin)  <br/>
 
 
 
