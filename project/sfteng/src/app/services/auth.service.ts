import { Injectable } from '@angular/core';
import { Router } from  "@angular/router";
import * as firebase from 'firebase';
import { AngularFireAuth } from  "@angular/fire/auth";
import { User } from  'firebase';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  user: User;
  constructor(public afAuth:AngularFireAuth,public router:Router) {
    this.afAuth.authState.subscribe(user => {
      if (user){
        this.user = user;
        localStorage.setItem('user', JSON.stringify(this.user));
      } else {
        localStorage.setItem('user', null);
      }
    })
   }

  async  loginWithGoogle(){
    await  this.afAuth.signInWithPopup(new firebase.auth.GoogleAuthProvider())
    this.router.navigate(['/page']);
  }

  async logout(){
    await this.afAuth.signOut();
    localStorage.removeItem('user');
    this.router.navigate(['']);
  }

  isLoggedIn(): boolean {
    const  user  =  JSON.parse(localStorage.getItem('user'));
    return  user  !==  null;
  }


}
