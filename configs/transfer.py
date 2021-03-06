class config():

    board_size       = 9
    transfer         = True
    prev_board_size  = 5

    # env config
    render_train     = False
    render_test      = False
    overwrite_render = True
    record           = False
    high             = 255.


    # output config
    #output_path  = "results/q2_linear/" 
    output_path = 'results/%dx%d_save/' % (board_size, board_size)
    prev_output_path = 'results/%dx%d_save/' % (prev_board_size, prev_board_size)
    model_output = output_path + "save"
    log_path     = output_path + "log.txt"
    plot_output  = output_path + "scores.png"

    # model and training config
    num_episodes_test = 20
    grad_clip         = True
    clip_val          = 10
    saving_freq       = 5000
    log_freq          = 50
    eval_freq         = 1000
    soft_epsilon      = 0

    # hyper params
    nsteps_train       = 100 # increasing this was necessary
    batch_size         = 32
    buffer_size        = 1000
    target_update_freq = 500
    gamma              = 0.99
    learning_freq      = 4
    state_history      = 1 # Changed this - was 4, now is 1. Don't think state history should matter for GO, except maybe for ko?
    lr_begin           = 0.005
    lr_end             = 0.001
    lr_nsteps          = nsteps_train/2
    eps_begin          = 1
    eps_end            = 0.01
    eps_nsteps         = nsteps_train/2
    learning_start     = 200
