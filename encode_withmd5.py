import hashlib

d = {
	"cac:PartyIdentification": 1,
	"cbc:Name": 2,
	"cbc:CitySubdivisionName": 3,
	"cbc:TaxAmount": 4,
	"cbc:ID": 5,
	"cac:AdditionalDocumentReference": 6,
	"cac:TaxScheme": 7,
	"cbc:CalculationSequenceNumeric": 8,
	"cbc:LineExtensionAmount": 9,
	"cac:PostalAddress": 10,
	"cbc:TaxTypeCode": 11,
	"cbc:TaxableAmount": 12,
	"cac:TaxSubtotal": 13,
	"cac:TaxCategory": 14,
	"cbc:IssueDate": 15,
	"cbc:ElectronicMail": 16,
	"ds:DigestValue": 17,
	"cbc:BuildingNumber": 18,
	"cac:PartyName": 19,
	"cbc:CityName": 20,
	"cbc:StreetName": 21,
	"cac:Country": 22,
	"cbc:DocumentTypeCode": 23,
	"cac:PartyTaxScheme": 24,
	"cbc:PostalZone": 25,
	"cbc:EmbeddedDocumentBinaryObject": 26,
	"cbc:Percent": 27,
	"xades:SignedSignatureProperties": 28,
	"cbc:InvoicedQuantity": 29,
	"cac:DigitalSignatureAttachment": 30,
	"cac:TaxTotal": 31,
	"cac:Contact": 32,
	"cbc:Telephone": 33,
	"xades:SignedDataObjectProperties": 34,
	"cbc:Note": 35,
	"cac:AccountingSupplierParty": 36,
	"cac:AccountingCustomerParty": 37,
	"cbc:BuildingName": 38,
	"xades:QualifyingProperties": 39,
	"ds:Reference": 40,
	"xades:SigningCertificate": 41,
	"cbc:DocumentCurrencyCode": 42,
	"cbc:WebsiteURI": 43,
	"cac:InvoiceLine": 44,
	"cbc:PriceAmount": 45,
	"ds:DigestMethod": 46,
	"xades:SignedProperties": 47,
	"cac:LegalMonetaryTotal": 48,
	"cbc:TaxExclusiveAmount": 49,
	"cbc:TaxInclusiveAmount": 50,
	"cac:ExternalReference": 51,
	"ext:ExtensionContent": 52,
	"cbc:LineCountNumeric": 53,
	"cbc:DocumentType": 54,
	"xades:DataObjectFormat": 55,
	"ds:X509SerialNumber": 56,
	"cbc:CustomizationID": 57,
	"cbc:InvoiceTypeCode": 58,
	"cac:Party": 59,
	"cac:AllowanceCharge": 60,
	"cbc:ChargeIndicator": 61,
	"cbc:Telefax": 62,
	"ds:X509Certificate": 63,
	"xades:IssuerSerial": 64,
	"xades:ClaimedRoles": 65,
	"cac:SignatoryParty": 66,
	"ext:UBLExtensions": 67,
	"ds:SignatureValue": 68,
	"xades:SigningTime": 69,
	"ds:X509IssuerName": 70,
	"xades:ClaimedRole": 71,
	"cbc:CopyIndicator": 72,
	"cbc:PayableAmount": 73,
	"cbc:MultiplierFactorNumeric": 74,
	"cac:SellersItemIdentification": 75,
	"ext:UBLExtension": 76,
	"xades:CertDigest": 77,
	"xades:SignerRole": 78,
	"cbc:UBLVersionID": 79,
	"cbc:Region": 80,
	"cbc:District": 81,
	"cbc:AllowanceTotalAmount": 82,
	"ds:RSAKeyValue": 83,
	"cac:Attachment": 84,
	"cac:Price": 85,
	"ds:SignedInfo": 86,
	"ds:Transforms": 87,
	"cbc:ProfileID": 88,
	"cac:Signature": 89,
	"ds:CanonicalizationMethod": 90,
	"xades:MimeType": 91,
	"cac:Item": 92,
	"ds:Signature": 93,
	"cbc:Room": 94,
	"ds:X509Data": 95,
	"ds:KeyValue": 96,
	"ds:Exponent": 97,
	"cbc:PaymentDueDate": 98,
	"ds:KeyInfo": 99,
	"ds:Modulus": 100,
	"xades:Cert": 101,
	"cbc:Amount": 102,
	"ds:SignatureMethod": 103,
	"ds:Object": 104,
	"cbc:BaseAmount": 105,
	"cbc:UUID": 106,
	"cbc:AllowanceChargeReason": 107,
	"cac:PayeeFinancialAccount": 108,
	"cbc:URI": 109,
	"Invoice": 110,
	"cac:PaymentTerms": 111,
	"cbc:ChargeTotalAmount": 112,
	"cac:FinancialInstitutionBranch": 113,
	"cbc:PaymentMeansCode": 114,
	"cbc:TaxExemptionReasonCode": 115,
	"ds:Transform": 116,
	"cbc:IssueTime": 117,
	"cac:FinancialInstitution": 118,
	"cbc:TaxExemptionReason": 119,
	"cac:PaymentMeans": 120,
	"cac:WithholdingTaxTotal": 121,
	"cac:BuyersItemIdentification": 122,
	"cbc:PayableRoundingAmount": 123,
	"cbc:CurrencyCode": 124,
	"cac:DespatchDocumentReference": 125,
	"cbc:PaymentAlternativeCurrencyCode": 126,
	"cbc:IdentificationCode": 127,
	"cbc:PricingCurrencyCode": 128,
	"cbc:PaymentCurrencyCode": 129,
	"cbc:SequenceNumeric": 130,
	"cac:ManufacturersItemIdentification": 131,
	"cbc:TaxCurrencyCode": 132,
	"cbc:DocumentDescription": 133,
	"cbc:SourceCurrencyCode": 134,
	"cbc:TargetCurrencyCode": 135,
	"cac:Delivery": 136,
	"cbc:CalculationRate": 137,
	"cbc:Description": 138,
	"ds:X509SubjectName": 139,
	"cac:AgentParty": 140,
	"cac:BuyerCustomerParty": 141,
	"cbc:TransactionCurrencyTaxAmount": 142,
	"cbc:FamilyName": 143,
	"cbc:FirstName": 144,
	"cac:PricingExchangeRate": 145,
	"cac:OriginCountry": 146,
	"cac:Person": 147,
	"cac:AdditionalItemIdentification": 148,
	"cac:OrderReference": 149,
	"cbc:BaseUnitMeasure": 150,
	"cac:DeliveryAddress": 151,
	"cbc:InstructionNote": 152,
	"cbc:PerUnitAmount": 153,
	"cac:DespatchLineReference": 154,
	"cbc:TransportModeCode": 155,
	"cac:DocumentReference": 156,
	"cac:CommodityClassification": 157,
	"cbc:ItemClassificationCode": 158,
	"cac:TransportHandlingUnit": 159,
	"cbc:PaymentNote": 160,
	"cbc:Date": 161,
	"cbc:AccountingCost": 162,
	"cac:PaymentAlternativeExchangeRate": 163,
	"cac:DeliveryTerms": 164,
	"cac:ShipmentStage": 165,
	"cbc:RequiredCustomsID": 166,
	"cac:PartyLegalEntity": 167,
	"cbc:RegistrationName": 168,
	"cac:Shipment": 169,
	"cbc:DeclaredCustomsValueAmount": 170,
	"cac:GoodsItem": 171,
	"cac:PaymentExchangeRate": 172,
	"cac:ActualPackage": 173,
	"cbc:PackagingTypeCode": 174,
	"cac:MaritimeTransport": 175,
	"cac:PhysicalLocation": 176,
	"cbc:LineID": 177,
	"cbc:ModelName": 178,
	"cbc:CompanyID": 179,
	"cac:TaxExchangeRate": 180,
	"cac:TransportMeans": 181,
	"cbc:DeclaredForCarriageValueAmount": 182,
	"cac:InvoiceDocumentReference": 183,
	"cbc:BrandName": 184,
	"cbc:InsuranceValueAmount": 185,
	"cbc:VesselID": 186,
	"cac:Address": 187,
	"cbc:Keyword": 188,
	"cac:BillingReference": 189,
	"cac:DeliveryParty": 190,
	"cbc:MiddleName": 191,
	"cbc:PaymentChannelCode": 192,
	'..\\xsdrt\\maindoc\\UBL-Invoice-2.1.xsd"': 193,
	'Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature"': 194,
	'Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"': 195,
	'Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"': 196,
	'Algorithm="http://www.w3.org/TR/2001/REC-xml-c14n-20010315"': 197,
	'Type="http://uri.etsi.org/01903#SignedProperties"': 198,
	'characterSetCode="UTF-8"': 199,
	'currencyID="TRY"': 200,
	'encodingCode="Base64"': 201,
	'mimeCode="application/xml"': 202,
	'schemeID="MERSISNO"': 203,
	'schemeID="TICARETSICILNO"': 204,
	'schemeID="VKN"': 205,
	'schemeID="VKN_TCKN"': 206,
	'unitCode="C62"': 207,
	'xmlns:cac="urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"': 208,
	'xmlns:cbc="urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"': 209,
	'xmlns:ds="http://www.w3.org/2000/09/xmldsig#"': 210,
	'xmlns:ext="urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2"': 211,
	'xmlns:xades="http://uri.etsi.org/01903/v1.3.2#"': 212,
	'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"': 213,
	'xmlns="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2"': 214,
	'xsi:schemaLocation="urn:oasis:names:specification:ubl:schema:xsd:Invoice-2': 215,

}

def encode_md5(in_file, out_file):

	fin = open(in_file)
	#fin = open("in.xml")
	contents = fin.read()
	fin.close()

	fout = open(out_file, "w")

	started = False

	s = ""
	save = False

	for c in contents:

		s += c

		if c == '<':
			# begining of a new tagi flush old ones
			if save:
				xlst = s[:-1]
				xlst_hash = hashlib.md5(xlst.encode("UTF-8")).hexdigest()
				f2 = open("xlst/" + xlst_hash, "w")
				f2.write(xlst)
				f2.close()
				s = xlst_hash + "<"

			fout.write(s)
			s = ""
		elif c == '>':

			tags = s[:-1].split(" ")

			pre = ""
			post = ""
			s = ""
			parts = []

			for tag in tags:
				if tag[0] == "/":
					tag = tag[1:]
					pre = "/"
				if tag[-1] == "/":
					tag = tag[:-1]
					post = "/"

				if tag == "cbc:EmbeddedDocumentBinaryObject":
					save = not save

				#print(tag)
				if tag in d:
					parts.append(pre + str(d[tag]) + post)
				else:
					parts.append (pre + tag + post)

			s += " ".join(parts) + ">"
			fout.write(s)
			s = ""
			

	if s != "":
		fout.write(s)

	fout.close()

if __name__ == "__main__":
	encode_md5("../son_veri/EXTRACTED/e68b5694-276b-4f3a-8405-acc95e3e15aa.xml", "out_md5.xml")
