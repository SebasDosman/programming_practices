import { Component, OnInit } from "@angular/core";
import { FormControl } from "@angular/forms";

@Component({
   selector: "app-main",
   templateUrl: "./login.component.html",
   styleUrls: ["./login.component.css"]
})

export class LoginComponent implements OnInit {
  public inputControl : any;
  public hide : boolean = true;

  constructor() {
  }

  public ngOnInit(): void {
    this.inputControl = new FormControl();
  }
}
