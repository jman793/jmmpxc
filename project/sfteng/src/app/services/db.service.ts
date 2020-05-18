import { Injectable } from '@angular/core';
import { AngularFirestore } from '@angular/fire/firestore';
import { AngularFirestoreCollection } from '@angular/fire/firestore/public_api';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DbService {

  collection:string;
  docs;

  constructor(private db: AngularFirestore) {
    if(localStorage.getItem('user')!='null'){
      this.collection=JSON.parse(localStorage.getItem('user')).displayName 
    }
    else
      this.collection='guest';
    
   }

   insert(object:Object):void{
    if(this.collection=='guest')
      return;
    
    this.db.collection(this.collection).add(object);
   }

    
   pull():Observable<unknown>{
     return this.db.collection(this.collection).valueChanges();
   }

}
