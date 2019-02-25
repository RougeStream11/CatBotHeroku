import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord import Game
import asyncio
from itertools import cycle
import json
import time
import os
import random
import hashlib
import async

client = commands.Bot(command_prefix = '%')
client.remove_command('help')
status  = ["Cat Bot V1.3", "Running on Pydroid", "Currently on " + format(len(client.servers)) + " servers", "Prefix is %"]

players = {}

catfacts = ["Unlike dogs, cats do not have a sweet tooth. Scientists believe this is due to a mutation in a key taste receptor",
"When a cat chases its prey, it keeps its head level. Dogs and humans bob their heads up and down",
"The technical term for a cat’s hairball is a bezoar",
"A group of cats is called a clowder.",
"A cat can’t climb head first down a tree because every claw on a cat’s paw points the same way. To get down from a tree, a cat must back down.",
"Cats make about 100 different sounds. Dogs make only about 10.",
"Every year, nearly four million cats are eaten in Asia.",
"There are more than 500 million domestic cats in the world, with approximately 40 recognized breeds.",
"Approximately 24 cat skins can make a coat.",
"While it is commonly thought that the ancient Egyptians were the first to domesticate cats, the oldest known pet cat was recently found in a 9,500-year-old grave on the Mediterranean island of Cyprus. This grave predates early Egyptian art depicting cats by 4,000 years or more.",
"During the time of the Spanish Inquisition, Pope Innocent VIII condemned cats as evil and thousands of cats were burned. Unfortunately, the widespread killing of cats led to an explosion of the rat population, which exacerbated the effects of the Black Death.",
"During the Middle Ages, cats were associated with withcraft, and on St. John’s Day, people all over Europe would stuff them into sacks and toss the cats into bonfires. On holy days, people celebrated by tossing cats from church towers.",
"The first cat in space was a French cat named Felicette (a.k.a. “Astrocat”) In 1963, France blasted the cat into outer space. Electrodes implanted in her brains sent neurological signals back to Earth. She survived the trip.",
"The group of words associated with cat (catt, cath, chat, katze) stem from the Latin catus, meaning domestic cat, as opposed to feles, or wild cat.",
"The term “puss” is the root of the principal word for “cat” in the Romanian term pisica and the root of secondary words in Lithuanian (puz) and Low German puus. Some scholars suggest that “puss” could be imitative of the hissing sound used to get a cat’s attention. As a slang word for the female pudenda, it could be associated with the connotation of a cat being soft, warm, and fuzzy.",
"Approximately 40,000 people are bitten by cats in the U.S. annually.",
"Cats are North America’s most popular pets: there are 73 million cats compared to 63 million dogs. Over 30% of households in North America own a cat.",
"According to Hebrew legend, Noah prayed to God for help protecting all the food he stored on the ark from being eaten by rats. In reply, God made the lion sneeze, and out popped a cat.",
"A cat’s hearing is better than a dog’s. And a cat can hear high-frequency sounds up to two octaves higher than a human.",
"A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance.",
"A cat rubs against people not only to be affectionate but also to mark out its territory with scent glands around its face. The tail area and paws also carry the cat’s scent.",
"Researchers are unsure exactly how a cat purrs. Most veterinarians believe that a cat purrs by vibrating vocal folds deep in the throat. To do this, a muscle in the larynx opens and closes the air passage about 25 times per second.",
"When a family cat died in ancient Egypt, family members would mourn by shaving off their eyebrows. They also held elaborate funerals during which they drank wine and beat their breasts. The cat was embalmed with a sculpted wooden mask and the tiny mummy was placed in the family tomb or in a pet cemetery with tiny mummies of mice.",
"In 1888, more than 300,000 mummified cats were found an Egyptian cemetery. They were stripped of their wrappings and carted off to be used by farmers in England and the U.S. for fertilizer.",
"Most cats give birth to a litter of between one and nine kittens. The largest known litter ever produced was 19 kittens, of which 15 survived.",
"Smuggling a cat out of ancient Egypt was punishable by death. Phoenician traders eventually succeeded in smuggling felines, which they sold to rich people in Athens and other important cities.",
"The earliest ancestor of the modern cat lived about 30 million years ago. Scientists called it the Proailurus, which means “first cat” in Greek. The group of animals that pet cats belong to emerged around 12 million years ago.",
"The biggest wildcat today is the Siberian Tiger. It can be more than 12 feet (3.6 m) long (about the size of a small car) and weigh up to 700 pounds (317 kg).",
"A cat’s brain is biologically more similar to a human brain than it is to a dog’s. Both humans and cats have identical regions in their brains that are responsible for emotions.",
"Many Egyptians worshipped the goddess Bast, who had a woman’s body and a cat’s head.",
"Mohammed loved cats and reportedly his favorite cat, Muezza, was a tabby. Legend says that tabby cats have an “M” for Mohammed on top of their heads because Mohammad would often rest his hand on the cat’s head.",
"While many parts of Europe and North America consider the black cat a sign of bad luck, in Britain and Australia, black cats are considered lucky.",
"The most popular pedigreed cat is the Persian cat, followed by the Main Coon cat and the Siamese cat.",
"The smallest pedigreed cat is a Singapura, which can weigh just 4 lbs (1.8 kg), or about five large cans of cat food. The largest pedigreed cats are Maine Coon cats, which can weigh 25 lbs (11.3 kg), or nearly twice as much as an average cat weighs.",
"Some cats have survived falls of over 65 feet (20 meters), due largely to their “righting reflex.” The eyes and balance organs in the inner ear tell it where it is in space so the cat can land on its feet. Even cats without a tail have this ability.",
"Some Siamese cats appear cross-eyed because the nerves from the left side of the brain go to mostly the right eye and the nerves from the right side of the brain go mostly to the left eye. This causes some double vision, which the cat tries to correct by “crossing” its eyes.",
"Researchers believe the word “tabby” comes from Attabiyah, a neighborhood in Baghdad, Iraq. Tabbies got their name because their striped coats resembled the famous wavy patterns in the silk produced in this city.",
"A cat can jump up to five times its own height in a single bound.",
"Cats hate the water because their fur does not insulate well when it’s wet. The Turkish Van, however, is one cat that likes swimming. Bred in central Asia, its coat has a unique texture that makes it water resistant.",
"The Egyptian Mau is probably the oldest breed of cat. In fact, the breed is so ancient that its name is the Egyptian word for “cat.”",
"The first commercially cloned pet was a cat named 'Little Nicky'. He cost his owner $50,000, making him one of the most expensive cats ever.",
"A cat usually has about 12 whiskers on each side of its face.",
"A cat’s eyesight is both better and worse than humans. It is better because cats can see in much dimmer light and they have a wider peripheral view. It’s worse because they don’t see color as well as humans do. Scientists believe grass appears red to cats.",
"Spanish-Jewish folklore recounts that Adam’s first wife, Lilith, became a black vampire cat, sucking the blood from sleeping babies. This may be the root of the superstition that a cat will smother a sleeping baby or suck out the child’s breath.",
"Perhaps the most famous comic cat is the Cheshire Cat in Lewis Carroll’s Alice in Wonderland. With the ability to disappear, this mysterious character embodies the magic and sorcery historically associated with cats.",
"The smallest wildcat today is the Black-footed cat. The females are less than 20 inches (50 cm) long and can weigh as little as 2.5 lbs (1.2 kg).",
"On average, cats spend 2/3 of every day sleeping. That means a nine-year-old cat has been awake for only three years of its life.",
"In the original Italian version of Cinderella, the benevolent fairy godmother figure was a cat.",
"The little tufts of hair in a cat’s ear that help keep out dirt direct sounds into the ear, and insulate the ears are called “ear furnishings.”",
"The ability of a cat to find its way home is called “psi-traveling.” Experts think cats either use the angle of the sunlight to find their way or that cats have magnetized cells in their brains that act as compasses.",
"Isaac Newton invented the cat flap. Newton was experimenting in a pitch-black room. Spithead, one of his cats, kept opening the door and wrecking his experiment. The cat flap kept both Newton and Spithead happy.",
"The world’s rarest coffee, Kopi Luwak, comes from Indonesia where a wildcat known as the luwak lives. The cat eats coffee berries and the coffee beans inside pass through the stomach. The beans are harvested from the cat’s dung heaps and then cleaned and roasted. Kopi Luwak sells for about $500 for a 450 g (1 lb) bag.",
"A cat’s jaw can’t move sideways, so a cat can’t chew large chunks of food.",
"Cats don't actually meow at each other, just at humans. Cats typically will spit, purr, and hiss at other cats.",
"Female cats tend to be right pawed, while male cats are more often left pawed. Interestingly, while 90% of humans are right handed, the remaining 10% of lefties also tend to be male.",
"A cat’s back is extremely flexible because it has up to 53 loosely fitting vertebrae. Humans only have 34.",
"All cats have claws, and all except the cheetah sheath them when at rest.",
"Two members of the cat family are distinct from all others: the clouded leopard and the cheetah. The clouded leopard does not roar like other big cats, nor does it groom or rest like small cats. The cheetah is unique because it is a running cat; all others are leaping cats. They are leaping cats because they slowly stalk their prey and then leap on it.",
"A cat lover is called an Ailurophilia (Greek: cat+lover).",
"In Japan, cats are thought to have the power to turn into super spirits when they die. This may be because according to the Buddhist religion, the body of the cat is the temporary resting place of very spiritual people.",
"Most cats had short hair until about 100 years ago, when it became fashionable to own cats and experiment with breeding.",
"One reason that kittens sleep so much is because a growth hormone is released only during sleep.",
"Cats have about 130,000 hairs per square inch (20,155 hairs per square centimeter).",
"The heaviest cat on record is Himmy, a Tabby from Queensland, Australia. He weighed nearly 47 pounds (21 kg). He died at the age of 10.",
"The oldest cat on record was Crème Puff from Austin, Texas, who lived from 1967 to August 6, 2005, three days after her 38th birthday. A cat typically can live up to 20 years, which is equivalent to about 96 human years.",
"The lightest cat on record is a blue point Himalayan called Tinker Toy, who weighed 1 pound, 6 ounces (616 g). Tinker Toy was 2.75 inches (7 cm) tall and 7.5 inches (19 cm) long.",
"Approximately 1/3 of cat owners think their pets are able to read their minds.",
"Approximately 1/3 of cat owners think their pets are able to read their minds.",
"A commemorative tower was built in Scotland for a cat named Towser, who caught nearly 30,000 mice in her lifetime.",
"In the 1750s, Europeans introduced cats into the Americas to control pests.",
"The first cat show was organized in 1871 in London. Cat shows later became a worldwide craze.",
"The first cartoon cat was Felix the Cat in 1919. In 1940, Tom and Jerry starred in the first theatrical cartoon “Puss Gets the Boot.” In 1981 Andrew Lloyd Weber created the musical Cats, based on T.S. Eliot’s Old Possum’s Book of Practical Cats.",
"The normal body temperature of a cat is between 100.5 ° and 102.5 °F. A cat is sick if its temperature goes below 100 ° or above 103 °F.",
"A cat has 230 bones in its body. A human has 206. A cat has no collarbone, so it can fit through any opening the size of its head.",
"Cats have 32 muscles that control the outer ear (humans have only 6). A cat can independently rotate its ears 180 degrees.",
"A cat’s nose pad is ridged with a unique pattern, just like the fingerprint of a human.",
"If they have ample water, cats can tolerate temperatures up to 133 °F.",
"Foods that should not be given to cats include onions, garlic, green tomatoes, raw potatoes, chocolate, grapes, and raisins. Though milk is not toxic, it can cause an upset stomach and gas. Tylenol and aspirin are extremely toxic to cats, as are many common houseplants. Feeding cats dog food or canned tuna that’s for human consumption can cause malnutrition.",
"A 2007 Gallup poll revealed that both men and women were equally likely to own a cat.",
"A cat’s heart beats nearly twice as fast as a human heart, at 110 to 140 beats a minute.",
"In just seven years, a single pair of cats and their offspring could produce a staggering total of 420,000 kittens.",
"Relative to its body size, the clouded leopard has the biggest canines of all animals’ canines. Its dagger-like teeth can be as long as 1.8 inches (4.5 cm).",
"Cats spend nearly 1/3 of their waking hours cleaning themselves.",
"Grown cats have 30 teeth. Kittens have about 26 temporary teeth, which they lose when they are about 6 months old.",
"Cats don’t have sweat glands over their bodies like humans do. Instead, they sweat only through their paws.",
"A cat called Dusty has the known record for the most kittens. She had more than 420 kittens in her lifetime.",
"The largest cat breed is the Ragdoll. Male Ragdolls weigh between 12 and 20 lbs (5.4-9.0 k). Females weigh between 10 and 15 lbs (4.5-6.8 k).",
"Cats are extremely sensitive to vibrations. Cats are said to detect earthquake tremors 10 or 15 minutes before humans can.",
"In contrast to dogs, cats have not undergone major changes during their domestication process.",
"A female cat is called a queen or a molly.",
"In the 1930s, two Russian biologists discovered that color change in Siamese kittens depend on their body temperature. Siamese cats carry albino genes that work only when the body temperature is above 98° F. If these kittens are left in a very warm room, their points won’t darken and they will stay a creamy white.",
"There are up to 60 million feral cats in the United States alone.",
"The oldest cat to give birth was Kitty who, at the age of 30, gave birth to two kittens. During her life, she gave birth to 218 kittens.",
"The most traveled cat is Hamlet, who escaped from his carrier while on a flight. He hid for seven weeks behind a panel on the airplane. By the time he was discovered, he had traveled nearly 373,000 miles (600,000 km).",
"In Holland’s embassy in Moscow, Russia, the staff noticed that the two Siamese cats kept meowing and clawing at the walls of the building. Their owners finally investigated, thinking they would find mice. Instead, they discovered microphones hidden by Russian spies. The cats heard the microphones when they turned on.",
"The most expensive cat was an Asian Leopard cat (ALC)-Domestic Shorthair (DSH) hybrid named Zeus. Zeus, who is 90% ALC and 10% DSH, has an asking price of £100,000 ($154,000).",
"The cat who holds the record for the longest non-fatal fall is Andy. He fell from the 16th floor of an apartment building (about 200 ft/.06 km) and survived.",
"Rome has more homeless cats per square mile than any other city in the world.",
"The richest cat is Blackie who was left £15 million by his owner, Ben Rea.",
"The claws on the cat’s back paws aren’t as sharp as the claws on the front paws because the claws in the back don’t retract and, consequently, become worn."]

dogfacts = ["All dogs can be traced back 40 million years ago to a weasel-like animal called the Miacis which dwelled in trees and dens. The Miacis later evolved into the Tomarctus, a direct forbear of the genus Canis, which includes the wolf and jackal as well as the dog.",
"Small quantities of grapes and raisins can cause renal failure in dogs. Chocolate, macadamia nuts, cooked onions, or anything with caffeine can also be harmful.",
"Apple and pear seeds contain arsenic, which may be deadly to dogs.",
"Dogs have sweat glands in between their paws.",
"In 2003, Dr. Roger Mugford invented the “wagometer,” a device that claims to interpret a dog’s exact mood by measuring the wag of its tail.",
"Ancient Egyptians revered their dogs. When a pet dog would die, the owners shaved off their eyebrows, smeared mud in their hair, and mourned aloud for days.",
"Dogs have three eyelids. The third lid, called a nictitating membrane or “haw,” keeps the eye lubricated and protected.",
"A dog’s shoulder blades are unattached to the rest of the skeleton to allow greater flexibility for running.",
"Puppies are sometimes rejected by their mother if they are born by cesarean and cleaned up before being given back to her.",
"The phrase “raining cats and dogs” originated in seventeenth-century England. During heavy rainstorms, many homeless animals would drown and float down the streets, giving the appearance that it had actually rained cats and dogs.",
"During the Middle Ages, Great Danes and Mastiffs were sometimes suited with armor and spiked collars to enter a battle or to defend supply caravans.",
"Pekingese and Japanese Chins were so important in the ancient Far East that they had their own servants and were carried around trade routes as gifts for kings and emperors. Pekingese were even worshipped in the temples of China for centuries.",
"After the fall of Rome, human survival often became more important than breeding and training dogs. Legends of werewolves emerged during this time as abandoned dogs traveling in packs commonly roamed streets and terrified villagers.",
"The most dogs ever owned by one person were 5,000 Mastiffs owned by Kublai Khan.",
"The American Kennel Club, the most influential dog club in the United States, was founded in 1884.",
"The most popular male dog names are Max and Jake. The most popular female dog names are Maggie and Molly.",
"Weird dog laws include allowing police offers in Palding, Ohio, to bite a dog to quiet it. In Ventura County, California, cats and dogs are not allowed to have sex without a permit.",
"The first dog chapel was established in 2001. It was built in St. Johnsbury, Vermont, by Stephan Huneck, a children’s book author whose five dogs helped him recuperate from a serious illness.",
"Those born under the sign of the dog in Chinese astrology are considered to be loyal and discreet, though slightly temperamental.",
"In Iran, it is against the law to own a dog as a pet. However, if an owner can prove the dog is a guard or hunting dog, this restriction doesn’t apply. Muslim reticence concerning dogs is perhaps due to the fact that rabies has always been endemic in the Middle East.",
"The Mayans and Aztecs symbolized every tenth day with the dog, and those born under this sign were believed to have outstanding leadership skills.",
"The shape of a dog’s face suggests how long it will live. Dogs with sharp, pointed faces that look more like wolves typically live longer. Dogs with very flat faces, such as bulldogs, often have shorter lives.",
"The ancient Mbaya Indians of the Gran Chaco in South America believed that humans originally lived underground until dogs dug them up.",
"French poodles did not originate in France but in Germany (“poodle” comes from the German pudel or pudelhund, meaning “splashing dog”). Some scholars speculate the poodle’s puffs of hair evolved when hunters shaved the poodle for more efficient swimming, while leaving the pom-poms around the major joints to keep them warm.",
"The name of the dog on the Cracker Jacks box is Bingo. The Taco Bell Chihuahua is a rescued dog named Gidget.",
"The first dogs were self-domesticated wolves which, at least 12,000 years ago, became attracted to the first sites of permanent human habitation.",
"Dachshunds were bred to fight badgers in their dens.",
"Plato once said that “a dog has the soul of a philosopher.",
"Laika, a Russian stray, was the first living mammal to orbit the Earth, in the Soviet Sputnik spacecraft in 1957. Though she died in space, her daughter Pushnika had four puppies with President John F. Kennedy’s terrier, Charlie.",
"Dalmatians are completely white at birth.",
"The term “dog days of summer” was coined by the ancient Greeks and Romans to describe the hottest days of summer that coincided with the rising of the Dog Star, Sirius.",
"Alexander the Great is said to have founded and named a city Peritas, in memory of his dog.",
"In ancient Greece, kennels of dogs were kept at the sanctuary of Asclepius at Epidaurus. Dogs were frequently sacrificed there because they were plentiful, inexpensive, and easy to control. During the July 25 celebration of the kunophontis (“the massacre of dogs”), dog sacrifices were performed to appease the ancestors of Apollo’s son, Linos, who was devoured by dogs.",
"Dog trainers in ancient China were held in high esteem. A great deal of dog domestication also took place in China, especially dwarfing and miniaturization.",
"The ancient religion Zoroastrianism includes in its religious text titled the Zend Avesta a section devoted to the care and breeding of dogs.",
"The earliest European images of dogs are found in cave paintings dating back 12,000 years ago in Spain.",
"The dog was frequently depicted in Greek art, including Cerberus, the three-headed hound guarding the entrance to the underworld, and the hunting dogs which accompanied the virgin goddess of the chase, Diana.",
"During the Renaissance, detailed portraits of the dog as a symbol of fidelity and loyalty appeared in mythological, allegorical, and religious art throughout Europe, including works by Leonardo da Vinci, Diego Velázquez, Jan van Eyck, and Albrecht Durer.",
"Rock star Ozzy Osborne saved his wife Sharon’s Pomeranian from a coyote by tackling and wresting the coyote until it released the dog.",
"A puppy is born blind, deaf, and toothless.",
"The Basenji is the world’s only barkless dog.",
"A dog most likely interprets a smiling person as baring their teeth, which is an act of aggression.",
"The origin of amputating a dog’s tail may go back to the Roman writer Lucius Columella’s (A.D. 4-70) assertion that tail docking prevented rabies.",
"One of Shakespeare’s most mischievous characters is Crab, the dog belonging to Launce in the Two Gentlemen of Verona. The word “watchdog” is first found in The Tempest.",
"President Franklin Roosevelt created a minor international incident when he claimed he sent a destroyer to the Aleutian Islands just to pick up his Scottish Terrier, Fala, who had been left behind.",
"Within hours of the September 11, 2001, attack on the World Trade Center, specially trained dogs were on the scene, including German Shepherds, Labs, and even a few little Dachshunds.",
"It costs approximately $10,000 to train a federally certified search and rescue dog.",
"The smallest dog on record was a matchbox-size Yorkshire Terrier. It was 2.5 tall at the shoulder, 3.5 from nose tip to tail, and weighed only 4 ounces.",
"Hollywood’s first and arguably best canine superstar was Rin Tin Tin, a five-day-old German Shepherd found wounded in battle in WWI France and adopted by an American soldier, Lee Duncan. He would sign his own contracts with his paw print.",
"During the Middle Ages, mixed breeds of peasants’ dogs were required to wear blocks around their necks to keep them from breeding with noble hunting dogs. Purebred dogs were very expensive and hunting became the province of the rich.",
"At the end of WWI, the German government trained the first guide dogs for war-blinded soldiers.",
"A dog can locate the source of a sound in 1/600 of a second and can hear sounds four times farther away than a human can.",
"Touch is the first sense the dog develops. The entire body, including the paws, is covered with touch-sensitive nerve endings.",
"Eighteen muscles or more can move a dog’s ear.",
"The names of 77 ancient Egyptian dogs have been recorded. The names refer to color and character, such as Blackie, Ebony, Good Herdsman, Reliable, and Brave One.",
"In Egypt, a person bitten by a rabid dog was encouraged to eat the roasted liver of a dog infected with rabies to avoid contracting the disease. The tooth of a dog infected with rabies would also be put in a band tied to the arm of the person bitten. The menstrual blood of a female dog was used for hair removal, while dog genitals were used for preventing the whitening of hair.",
"In early Christian tradition, Saint Christopher, the patron saint of travelers, is sometimes depicted with a dog’s head.",
"The oldest known dog bones were found in Asia and date as far back as 10,000 B.C. The first identifiable dog breed appeared about 9000 B.C. and was probably a type of Greyhound dog used for hunting.",
"There are an estimated 400 million dogs in the world.",
"The U.S. has the highest dog population in the world. France has the second highest.",
"Scholars have argued over the metaphysical interpretation of Dorothy’s pooch, Toto, in the Wizard of Oz. One theory postulates that Toto represents Anubis, the dog-headed Egyptian god of death, because Toto consistently keeps Dorothy from safely returning home.",
"Dog nose prints are as unique as human finger prints and can be used to identify them.",
"Bloodhound dogs have a keen sense of smell and have been used since the Middle Ages to track criminals.",
"It is much easier for dogs to learn spoken commands if they are given in conjunction with hand signals or gestures.",
"Dogs in a pack are more likely to chase and hunt than a single dog on its own. Two dogs are enough to form a pack.",
"Dogs can see in color, though they most likely see colors similar to a color-blind human. They can see better when the light is low.",
"Dogs have lived with humans for over 14,000 years. Cats have lived with people for only 7,000 years.",
"Zorba, an English mastiff, is the biggest dog ever recorded. He weighed 343 pounds and measured 8’ 3 from his nose to his tail.",
"The average dog can run about 19 mph. Greyhounds are the fastest dogs on Earth and can run at speeds of 45 mph.",
"One female dog and her female children could produce 4,372 puppies in seven years.",
"The most popular dog breed in Canada, U.S., and Great Britain is the Labrador retriever.",
"Petting dogs is proven to lower blood pressure of dog owners.",
"Greyhounds appear to be the most ancient dog breed. “Greyhound” comes from a mistake in translating the early German name Greishund, which means “old (or ancient) dog,” not from the color gray.",
"The oldest dog on record was an Australian cattle dog named Bluey who lived 29 years and 5 months. In human years, that is more than 160 years old.",
"Most experts believe humans domesticated dogs before donkeys, horses, sheep, goats, cattle, cats, or chickens.",
"A person standing still 300 yards away is almost invisible to a dog. But a dog can easily identify its owner standing a mile away if the owner is waving his arms.",
"Dogs with big, square heads and large ears (like the Saint Bernard) are the best at hearing subsonic sounds.",
"In Croatia, scientists discovered that lampposts were falling down because a chemical in the urine of male dogs was rotting the metal.",
"Dogs can smell about 1,000-10,000 times better than humans. While humans have 5 million smell-detecting cells, dogs have more than 220 million. The part of the brain that interprets smell is also four times larger in dogs than in humans.",
"Some dogs can smell dead bodies under water, where termites are hiding, and natural gas buried under 40 feet of dirt. They can even detect cancer that is too small to be detected by a doctor and can find lung cancer by sniffing a person’s breath.",
"Dogs have a wet nose to collect more of the tiny droplets of smelling chemicals in the air.",
"Dogs like sweets a lot more than cats do. While cats have around only 473 taste buds, dogs have about 1,700 taste buds. Humans have approximately 9,000.",
"Different smells in the a dog’s urine can tell other dogs whether the dog leaving the message is female or male, old or young, sick or healthy, happy or angry.",
"Male dogs will raise their legs while urinating to aim higher on a tree or lamppost because they want to leave a message that they are tall and intimidating. Some wild dogs in Africa try to run up tree trunks while they are urinating to appear to be very large.",
"Countess Karlotta Libenstein of Germany left approximately $106 million to her Alsatin, Gunther III, when she died in 1992.",
"A lost Dachshund was found swallowed whole in the stomach of a giant catfish in Berlin on July 2003.",
"A person should never kick a dog facing him or her. Some dogs can bite 10 times before a human can respond.",
"In Australia, a man who was arrested for drug possession argued his civil rights were violated when the drug-sniffing dog nuzzled his crotch. While the judge dismissed the charges, they were later reinstated when a prosecutor pointed out that in the animal kingdom, crotch nuzzling was a friendly gesture.",
"The Beagle came into prominence in the 1300s and 1400s during the days of King Henry VII of England. Elizabeth I was fond of Pocket Beagles, which were only 9 high.",
"The best dog to reportedly attract a date is the Golden Retriever. The worst is the Pit Bull.",
"The Akita is one of the most challenging dogs to own. Some insurance companies have even characterized it as the #1 “bad dog” and may even raise an Akita owner’s homeowner insurance costs.",
"The Beagle and Collie are the nosiest dogs, while the Akbash Dog and the Basenji are the quietest.",
"One survey reports that 33% of dog owners admit they talk to their dogs on the phone or leave messages on answering machines while they are away.",
"Thirty percent of all Dalmatians are deaf in one or both ears. Because bulldogs have extremely short muzzles, many spend their lives fighting suffocation. Because Chihuahuas have such small skulls, the flow of spinal fluid can be restricted, causing hydrocephalus, a swelling of the brain.",
"Dogs are about as smart as a two- or three-year-old child. This means they can understand about 150-200 words, including signals and hand movements with the same meaning as words.",
"The grief suffered after a pet dog dies can be the same as that experienced after the death of a person.",
"There are almost 5 million dog bites per year; children are the main victims. Dog bites cause losses of over $1 billion a year.",
"The most intelligent dogs are reportedly the Border Collie and the Poodle, while the least intelligent dogs are the Afghan Hound and the Basenji.",
"One kind of Pekingese is referred to as a “sleeve” because it was bred to fit into a Chinese empress’ sleeves, which was how it was often carried around.",
"A group of pugs is called a 'grumble'."]

dank = ["You are 0% dank",
"You are 1% dank",
"You are 2% dank",
"You are 3% dank",
"You are 4% dank",
"You are 5% dank",
"You are 6% dank",
"You are 7% dank",
"You are 8% dank",
"You are 9% dank",
"You are 10% dank",
"You are 11% dank",
"You are 12% dank",
"You are 13% dank",
"You are 14% dank",
"You are 15% dank",
"You are 16% dank",
"You are 17% dank",
"You are 18% dank",
"You are 19% dank",
"You are 20% dank",
"You are 21% dank",
"You are 22% dank",
"You are 23% dank",
"You are 24% dank",
"You are 25% dank",
"You are 26% dank",
"You are 27% dank",
"You are 28% dank",
"You are 29% dank",
"You are 30% dank",
"You are 31% dank",
"You are 32% dank",
"You are 33% dank",
"You are 34% dank",
"You are 35% dank",
"You are 36% dank",
"You are 37% dank",
"You are 38% dank",
"You are 39% dank",
"You are 40% dank",
"You are 41% dank",
"You are 42% dank",
"You are 43% dank",
"You are 44% dank",
"You are 45% dank",
"You are 46% dank",
"You are 47% dank",
"You are 48% dank",
"You are 49% dank",
"You are 50% dank",
"You are 51% dank",
"You are 52% dank",
"You are 53% dank",
"You are 54% dank",
"You are 55% dank",
"You are 56% dank",
"You are 57% dank",
"You are 58% dank",
"You are 59% dank",
"You are 60% dank",
"You are 61% dank",
"You are 62% dank",
"You are 63% dank",
"You are 64% dank",
"You are 65% dank",
"You are 66% dank",
"You are 67% dank",
"You are 68% dank",
"You are 69% dank",
"You are 70% dank",
"You are 71% dank",
"You are 72% dank",
"You are 73% dank",
"You are 74% dank",
"You are 75% dank",
"You are 76% dank",
"You are 77% dank",
"You are 78% dank",
"You are 79% dank",
"You are 80% dank",
"You are 81% dank",
"You are 82% dank",
"You are 83% dank",
"You are 84% dank",
"You are 85% dank",
"You are 86% dank",
"You are 87% dank",
"You are 88% dank",
"You are 89% dank",
"You are 90% dank",
"You are 91% dank",
"You are 92% dank",
"You are 93% dank",
"You are 94% dank",
"You are 95% dank",
"You are 96% dank",
"You are 97% dank",
"You are 98% dank",
"You are 99% dank",
"You are 100% dank",
"You are 100.1 % dank"]

dab = ["You are 0% dab",
"You are 1% dab",
"You are 2% dab",
"You are 3% dab",
"You are 4% dab",
"You are 5% dab",
"You are 6% dab",
"You are 7% dab",
"You are 8% dab",
"You are 9% dab",
"You are 10% dab",
"You are 11% dab",
"You are 12% dab",
"You are 13% dab",
"You are 14% dab",
"You are 15% dab",
"You are 16% dab",
"You are 17% dab",
"You are 18% dab",
"You are 19% dab",
"You are 20% dab",
"You are 21% dab",
"You are 22% dab",
"You are 23% dab",
"You are 24% dab",
"You are 25% dab",
"You are 26% dab",
"You are 27% dab",
"You are 28% dab",
"You are 29% dab",
"You are 30% dab",
"You are 31% dab",
"You are 32% dab",
"You are 33% dab",
"You are 34% dab",
"You are 35% dab",
"You are 36% dab",
"You are 37% dab",
"You are 38% dab",
"You are 39% dab",
"You are 40% dab",
"You are 41% dab",
"You are 42% dab",
"You are 43% dab",
"You are 44% dab",
"You are 45% dab",
"You are 46% dab",
"You are 47% dab",
"You are 48% dab",
"You are 49% dab",
"You are 50% dab",
"You are 51% dab",
"You are 52% dab",
"You are 53% dab",
"You are 54% dab",
"You are 55% dab",
"You are 56% dab",
"You are 57% dab",
"You are 58% dab",
"You are 59% dab",
"You are 60% dab",
"You are 61% dab",
"You are 62% dab",
"You are 63% dab",
"You are 64% dab",
"You are 65% dab",
"You are 66% dab",
"You are 67% dab",
"You are 68% dab",
"You are 69% dab",
"You are 70% dab",
"You are 71% dab",
"You are 72% dab",
"You are 73% dab",
"You are 74% dab",
"You are 75% dab",
"You are 76% dab",
"You are 77% dab",
"You are 78% dab",
"You are 79% dab",
"You are 80% dab",
"You are 81% dab",
"You are 82% dab",
"You are 83% dab",
"You are 84% dab",
"You are 85% dab",
"You are 86% dab",
"You are 87% dab",
"You are 88% dab",
"You are 89% dab",
"You are 90% dab",
"You are 91% dab",
"You are 92% dab",
"You are 93% dab",
"You are 94% dab",
"You are 95% dab",
"You are 96% dab",
"You are 97% dab",
"You are 98% dab",
"You are 99% dab",
"You are 100% dab",
"You are 100.1 % dab"]

async def status_change():
	await client.wait_until_ready()
	msg = cycle(status)
	
	
	while not client.is_closed:
			current_status = next(msg)
			await client.change_presence(game=discord.Game(name=current_status, type = 1))
			await asyncio.sleep(10)
			
			
@client.event
async def on_ready():
	print('cat working')
	print ("" + client.user.name)
	print ("ID: " + client.user.id
    
@client.event
async def on_message(message):
	await client.process_commands(message)
	author = message.author
	content = message.content
	server = message.server
	channel = message.channel
	id = message.author.id
	print('{}: {}: {}: {}: {} '.format(server, channel, author, id, content))
	
	if message.content.upper() == "HELLO":
		print('Sending reply ( Привет ) ')
		await client.send_message(message.channel, "Привет")
		
	if "OOF" in message.content.upper():
			print('sending reply, ( roblex )')
			await client.send_message(message.channel, 'Roblex died')

		
	if message.content.upper() == "INFO":
		print("Sending reply ( Info ) ")
		await client.send_message(message.channel, "Made by rouge with Atom And notepad++ with help of GW Andrew#8744 TrueMLGPro#9247 and Leterax#6932 And ruined by Arojam123Kappa#2630 spam this guy and insult him for ruining hard work")
		
	if "FOO" in message.content.upper():
			print('Sending reply ( borlex )')
			await client.send_message(message.channel, "deiD xelboR")
	
	if "OWO" in message.content.upper():
		print('sending firry')
		await client.send_message(message.channel, "Are you a furry")
			
	if message.content.startswith('hey'):
		msg = 'hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
		
	with open('users.json', 'r') as f:
		users = json.load(f)
		
		await update_data(users, message.author)
		await add_experience(users, message.author, 10)
		await level_up(users, message.author, message.channel)
		
	with open('users.json', 'w') as f:
		json.dump(users, f)
		
	with open('log.txt', 'a') as f:
		server = message.server
		channel = message.channel
		author = message.author
		content = message.content
		f.write('{} {} {} {}'.format(server, channel, author, content))
		f.write('\n')
	

async def update_data(users, user):
	if not user.id in users:
		users[user.id] = {}
		print(type(users))
		users[user.id]['experience'] = 0
		users[user.id]['level'] = 1
		
async def add_experience(users, user, exp):
	users[user.id]['experience'] += exp

async def level_up(users, user, channel):
	experience = users[user.id]['experience']
	lvl_start = users[user.id]['level']
	lvl_end = int(experience ** (1/4))
	
	if lvl_start < lvl_end:
		await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
		users[user.id]['level'] = lvl_end
	
		
		
@client.command()
async def count():
	a = -0
	for i in range(0, 100000000):
		a = a + 1
		print(a)
		await client.say(a)

@client.command(pass_context = True)
async def ping(ctx):
    resp = await client.say('pong')
    diff = resp.timestamp - ctx.message.timestamp
    await client.say(f'Responsed in {1000*diff.total_seconds():.1f}ms.')

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    
@client.command()
async def spa(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
		while True:
			await client.say(output)

@client.command()
async def md5(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(hashlib.md5(output.encode('utf-8')).hexdigest())
	await client.say('thanks to TrueMLGPro#0001 for giving me his md5 encrypt code')
	
@client.command()
async def sha1(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(hashlib.sha1(output.encode('utf-8')).hexdigest())
	await client.say('thanks to TrueMLGPro#0001 for giving me his md5 encrypt code')
	
@client.command()
async def sha256(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(hashlib.sha256(output.encode('utf-8')).hexdigest())
	await client.say('thanks to TrueMLGPro#0001 for giving me his md5 encrypt code')
	
@client.command()
async def sha512(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(hashlib.sha512(output.encode('utf-8')).hexdigest())
	await client.say('thanks to TrueMLGPro#0001 for giving me his md5 encrypt code')
	
@client.command()
async def sha224(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(hashlib.sha224(output.encode('utf-8')).hexdigest())
	await client.say('thanks to TrueMLGPro#0001 for giving me his md5 encrypt code')
	
@client.command()
async def sha384(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(hashlib.sha384(output.encode('utf-8')).hexdigest())
	await client.say('thanks to TrueMLGPro#0001 for giving me his md5 encrypt code')
	
@client.command()
async def blake2b(*args):
	output = ''
	for word in args:
		output += word
		output += ' '
	await client.say(hashlib.blake2b(output.encode('utf-8')).hexdigest())
	await client.say('thanks to TrueMLGPro#0001 for giving me his md5 encrypt code')
	
@client.command(pass_context=True)
async def clear(ctx, amount=5):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages);
    await client.say('messages were deleted')


@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author


	Help = discord.Embed(
		colour = discord.Colour.blue()
	)
	Help.set_author(name='Help')
	Help.add_field(name='Help', value='Here are the commands https://cat-bot-development.webnode.com/commands/', inline=False)
	client.start_private_message(author)
	await client.send_message(author, embed=Help)

@client.command(pass_context=True)
async def join(ctx):
	await client.say('Python was not working so this command is deleted')
 #   channel = ctx.message.author.voice.voice_channel
#    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
	await client.say('Python was not working so this command is deleted')
#    server = ctx.message.server
#    voice_client = client.voice_client_in(server)
#    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx): #url
	await client.say('Python was not working so this command is deleted')
#    server = ctx.message.server
#    voice_client = client.voice_client_in(server)
#    player = await voice_client.create_ytdl_player(url)
#    players[server.id] = player
#    player.start()

@client.command(pass_context=True)
async def pause(ctx):
	await client.say('Python was not working so this command is deleted')
#    id = ctx.message.server.id
#    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
	await client.say('Python was not working so this command is deleted')
#    id = ctx.message.server.id
#    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
	await client.say('Python was not working so this command is deleted')
#    id = ctx.message.server.id
#    players[id].resume()

@client.command()
async def hmm():
	print('hmmmm cat sent')
	hmm = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	hmm.set_image(url='https://cdn.discordapp.com/emojis/511248259004629002.png?v=1')
	
	await client.say(embed=hmm)
	
@client.command()
async def trump():
	print('Trum sent')
	trump = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	trump.set_image(url='https://cdn.discordapp.com/emojis/511241513980919819.png?v=1')
	
	await client.say(embed=trump)
	
@client.command()
async def pig():
	print('pig sent')
	pig = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	pig.set_image(url='https://cdn.discordapp.com/attachments/514547106359541793/514861264485482496/th.png')
	
	await client.say(embed=pig)
	
@client.command()
async def mlg():
	print('mlg sent')
	mlg = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	mlg.set_image(url='https://cdn.discordapp.com/attachments/514676360665628703/514863402620026891/f49b5c205d9c659371422779cdf0c8d6.png')
	
	await client.say(embed=mlg)
	
@client.command()
async def gw():
	print('gw sent')
	gw = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	gw.set_image(url='https://cdn.discordapp.com/attachments/514676360665628703/514867137035370506/5b37f08b19485a2222e7ca8d4bc722e9.png')
	
	await client.say(embed=gw)
	
@client.command()
async def communism():
	print('communism sent')
	com = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	com.set_image(url='https://cdn.discordapp.com/attachments/514676484472963072/514891415998824459/com.jpg')
	
	await client.say(embed=com)
	
@client.command()
async def dog():
	print('dog sent')
	dog = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	dog.set_image(url='https://cdn.discordapp.com/emojis/511242565664768005.png?v=1')
	
	await client.say(embed=dog)
	
@client.command()
async def cat():
	print('cat sent')
	cat = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	cat.set_image(url='https://cdn.discordapp.com/attachments/514676360665628703/515173664224706561/animalcat.jpg')
	
	await client.say(embed=cat)
	
@client.command()
async def fbi():
	print('fbi sent')
	fbi = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	fbi.set_image(url='https://cdn.discordapp.com/attachments/495694461834100737/502507431776223242/FBI.gif')
	
	await client.say(embed=fbi)
	
@client.command()
async def gwhome():
	print('gw andrew homeowrk sent')
	home = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	home.set_image(url='https://cdn.discordapp.com/attachments/514676360665628703/515575981663059968/5b37f08b19485a2222e7ca8d4bc722e9_1.png')
	
	await client.say(embed=home)
	
@client.command()
async def mlghome():
	print('mlg andrew homeowrk sent')
	home1 = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	home1.set_image(url='https://cdn.discordapp.com/attachments/514676360665628703/515576628298907649/f49b5c205d9c659371422779cdf0c8d6_-_Copy.png')
	
	await client.say(embed=home1)
	
@client.command(pass_context=True)
async def invite(ctx):
	author = ctx.message.author


	Embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	Embed.set_author(name='Invite Link')
	Embed.add_field(name='Invite Link', value='Want to invite this bot to your server? if yes then here is the invite link : https://discordapp.com/api/oauth2/authorize?client_id=501070141866377236&permissions=8&scope=bot', inline=False)
	client.start_private_message(author)
	await client.send_message(author, embed=Embed)
	
@client.command()
async def pingd():
	print('pingd andrew homeowrk sent')
	ping = discord.Embed(
	colour = discord.Colour.blue()
		
)
	
	ping.set_image(url='https://cdn.discordapp.com/attachments/412536528561242116/512346989091094528/everyone.gif')
	
	await client.say(embed=ping)
	
@client.command()
async def catfact():
	embed = discord.Embed(title="Fun fact:", description=random.choice(catfacts), color=0xeee657)
	await client.say(embed=embed)
	
@client.command()
async def dogfact():
	embed = discord.Embed(title="Fun fact:", description=random.choice(dogfacts), color=0xeee657)
	await client.say(embed=embed)
	
@client.command()
async def dankrate():
	embed = discord.Embed(title="Your % of dank", description=random.choice(dank), color=0xeee657)
	await client.say(embed=embed)
	
@client.command()
async def dabrate():
	embed = discord.Embed(title="Your % of dab", description=random.choice(dab), color=0xeee658)
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def number():
	await client.say(random.randint(0, 1000000000000000000000000000000000000000000000000000000000000000-00000000))
	
@client.command(pass_context=True)
async def randomspam():
	while True:
		await client.say(random.randint(0, 1000000000000000000000000000000000000000000000000000000000000000-00000000))
	
@client.command(pass_context=True)
async def userinfo(ctx, member: discord.Member):
	user = discord.Embed(colour=discord.Colour.purple())
	user.set_author(name="{}'s info".format(member))
	user.set_thumbnail(url=member.avatar_url)
	user.add_field(name="Name:", value=member.name)
	user.add_field(name="ID:", value=member.id)			
	user.add_field(name="Nick:", value=member.nick)
	user.add_field(name="bot", value=member.bot)
	user.add_field(name="status:", value=member.status)
	user.add_field(name="voice chat:", value=member.voice_channel)
	user.add_field(name="account made:", value=member.created_at)
	user.add_field(name="joined  this server:", value=member.joined_at)
	user.add_field(name="playing:", value=member.game)
	user.add_field(name="highest Role:", value=member.top_role)
	user.add_field(name="perms:", value=member.server_permissions)
	await client.say(embed=user)
			


@client.event
async def on_member_join(member):
		server = member.server
		user = member
		client.start_private_message(member)
		await client.send_message(member, 'Welcome to {} {}'.format(server.name, user.mention))

		with open('users.json', 'r') as f:
			users = json.load(f)
		
		await update_data(users, member)
		
		with open('users.json', 'w') as f:
			json.dump(users, f)

client.loop.create_task(status_change())						
client.run(os.getenv('TOKEN'))
