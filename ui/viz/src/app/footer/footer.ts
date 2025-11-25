import {Component} from '@angular/core';
import {MatGridListModule} from '@angular/material/grid-list';

export interface Tile {
  color: string;
  cols: number;
  rows: number;
  text: string;
}


@Component({
  selector: 'app-footer',
  templateUrl: './footer.html',
  styleUrl: './footer.css',
  imports: [MatGridListModule],
})
export class Footer {
  tiles: Tile[] = [
    {text: 'Footer', cols: 4, rows: 1, color: 'lightgreen'},
  ];

}
