### Fill in these code snippets into Pandas_in_a_nutshell.ipynb to make them run. (This file is NOT a runnable python script!)


### One solution for task I
ax = random_numbers.hist(density=True, 
                        bins =100, 
                        color="pink") # added color argument
ax.plot(x, np.exp(-(x-mu)**2/(2*sigma**2))/(np.sqrt(2*np.pi)*sigma), 
        color = "C4") # added color argument
ax.set_xlabel("x")
ax.set_ylabel(r"$\delta$x")
ax.set_title("An abnormal Gaussian.")        










### Five solutions for task II

# solution 1., with deprecated function append()
country_df = country_df.append({'Country':'Kenya', 
                                'Capital':Nairobi, 
                                'Inhabitants Country in Mio':51.04}, 
                                ignore_index=True) 
                                
# solution 2. # by concatenating a 1-row-DataFrame
country_df = pd.concat([country_df,
           pd.DataFrame({"Country":["Kenya"],
                         "Capital":["Nairobi"],
                         "Inhabitants Country in Mio":[51.04]})])
                         
# solution 3. # by concatenating a transposed two-column DataFrame created from a dictionary
country_df = pd.concat([country_df,
           pd.DataFrame({"Country":"Kenya",
                         "Capital":"Nairobi",
                         "Inhabitants Country in Mio":51.04}.items()).set_index(0).T])

# solution 4. # by concatenating a transposed one-column DataFrame created from a list
country_df = pd.concat([country_df,
           pd.DataFrame(["Kenya", "Nairobi", 51.04], 
            index=["Country", "Capital", "Inhabitants Country in Mio"]).T
          ], 
          ignore_index=True)                      

# solution 5. # with loc; danger: you might overwrite a row.
country_df.loc[4] = ["Kenya", "Nairobi", 51.04]











### Two solutions for task III

# solution 1.
country_df_copy = country_df_copy.set_index("Country")
country_df_copy.loc["Spain", "Inhabitants Country in Mio"] -= 7.57
country_df_copy = country_df_copy.rename(index={"Spain":"Spain (wo Catalunya)"})
country_df_copy = country_df_copy.reset_index()
country_df_copy

# solution 2.
country_df_copy.loc[country_df_copy[country_df_copy["Country"]=="Spain"].index, "Inhabitants Country in Mio"]-=7.57
country_df_copy.loc[2, "Country"] = "Spain (wo Catalunya)"
country_df_copy


