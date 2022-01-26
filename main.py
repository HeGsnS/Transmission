
permuation_sampling = PermutationGame(model, reference, batch_size=args.sample_num, antithetical=args.antithetical)
estimated_shapley_value = permuation_sampling.shapley_value_estimation(x)