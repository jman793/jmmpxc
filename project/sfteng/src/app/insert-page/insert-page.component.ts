import { Component, OnInit } from '@angular/core';
import { DbService } from '../services/db.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-insert-page',
  templateUrl: './insert-page.component.html',
  styleUrls: ['./insert-page.component.css']
})
export class InsertPageComponent implements OnInit {

  constructor(private db:DbService,private router:Router) { }

  ngOnInit() {
  }

  enterdata(){
    const str=(<HTMLInputElement>document.getElementById("data")).value;
    try{
      const obj=JSON.parse(str);
      this.db.insert(obj);
    }
    catch(err){
      alert("Invalid json data follow proper json syntax")
      console.log(err)
    }
  }

  goHome(){
    this.router.navigate(['/page'])
  }

}
