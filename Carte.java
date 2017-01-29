package jeu;

import java.awt.Color;

public class Carte {

	private final Color couleur;
	private final Symbole motif;
	private final int valeur;
	private final boolean vide;
	
	/**
	 *  Constructeur de Carte Vide
	 */
	public Carte() {
		super();
		this.couleur=Color.DARK_GRAY;
		this.motif=Symbole.VIDE;
		this.valeur=-1;		
		this.vide=true;
	}	
	
	public Carte(int couleur, int valeur, Symbole motif) {
		super();
		this.motif = motif;
		this.valeur = valeur;
		this.couleur=Color.DARK_GRAY; //TODO
		this.vide=false;
	}

	public Color getCouleur() {
		return couleur;
	}

	public Symbole getMotif() {
		return motif;
	}

	public int getValeur() {
		return valeur;
	}

	public boolean isVide() {
		return vide;
	}
	
	
	
	
}
