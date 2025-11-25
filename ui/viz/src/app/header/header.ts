import {Component} from '@angular/core';
import {MatGridListModule} from '@angular/material/grid-list';
import {MatMenuModule} from '@angular/material/menu';
import {MatButtonModule} from '@angular/material/button';
export interface Tile {
  color: string;
  cols: number;
  rows: number;
  text: string;
}


@Component({
  selector: 'app-header',
  templateUrl: './header.html',
  styleUrl: './header.css',
  imports: [MatGridListModule, MatButtonModule, MatMenuModule],
})
export class Header {
  tiles: Tile[] = [
    {text: '', cols: 4, rows: 1, color: 'lightblue'},
  ];

}
