class Configuration:
    # Window config - Agora detecta automaticamente o tamanho da tela
    # window_width e window_height são definidos dinamicamente no main.py
    # para preencher 100% da tela do computador
    
    limit_image_memory = 10
    icon_size = 16
    icon_size_large = 32

    # Menu Principal
    menu_principal_background_color = "#555"

    # Tools Bar
    tools_bar_background_color = menu_principal_background_color

    # Image Comparator
    image_comparator_background_color = menu_principal_background_color

    # Side menu config
    side_menu_width = 350
    side_menu_height = 300
    side_background_color = menu_principal_background_color