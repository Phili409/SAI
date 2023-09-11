import UserConnection, seedMaker, playlistModifications, playlistDataSelection, DS
import os, platform, sys, time, threading, cursor, socket
global userConnection 
userConnection = UserConnection.userConnection()

class SAI:
    def __init__(self) -> None:
        self.userID = userConnection.current_user()['id']
                
    def UpdateData():
        playlistDataSelection.updateMasterDatabase()
        DS.getDataMetricsFromClusters()
        print("\nMaster Database Data Successfuly Updated\nKMeans Cluster Data Successfuly Updated")
        
    def DeletePlaylists():
        playlistModifications.deleteCreatedPlaylists()
        print("\nPast Playlists Successfuly Deleted")
    
    def PlaylistRecomendation(self):        
        while True:
            menuSelection = input("Select a valid choice...\nMenu\n-----------\n0 = Vibes\n1 = Energy\n2 = Reggeton\n3 = isSpanishVibes\n4 = isAsia\n5 = JYM\n")
            
            if menuSelection:
                if menuSelection.isdigit():
                    menuSelection = int(menuSelection)
                    match (menuSelection):
                        case 0|1|2|3|4|5:
                            break 
                        case _:
                            None
            print("\nInvalid input Try again...\n")
        playlistName = input("\nWhat would you like to name your playlist? ")
        createPlaylist = userConnection.user_playlist_create(user=self.userID, name=playlistName, public=True, collaborative=False)
        playlistID = createPlaylist['id']
        
        userConnection.user_playlist_add_tracks(user=self.userID, playlist_id=playlistID, tracks=seedMaker.getPlaylistTypeData(menuSelection))
        
        playlistModifications.updateLinkedPlaylists(playlistID=playlistID)
        print(f"{playlistName} created enjoy!")

    def ClearTerminal(self):
        CurrentTerminal = platform.system()
        if CurrentTerminal == "Windows": os.system('cls')
        else: os.system('clear')
        
    def Internet(self) -> bool:
        try:
            socket.create_connection(("8.8.8.8", 53))
            return True
        except OSError:
            pass
        return False
    
    def main_menu(self):
        while True:
            MenuSelection = input("\n.")
            
            
            

    
    
        
        
        
        
if __name__ == '__main__':
    SAI = SAI()
    SAI.main_menu()
    